import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224H_validator_result.json"


REQUIRED_FILES = [
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
    "R224H_teacher_default_leakage_static_precheck_report.md",
    "R224H_forbidden_token_scan_matrix.json",
    "R224H_teacher_facing_naturalized_samples.md",
    "R224H_review_ledger_trace_retention_check.md",
    "R224H_publication_status_notice.md",
]


FORBIDDEN_TOKENS = [
    "unit_phase_role",
    "lesson_position_in_unit",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
    "router_effect",
    "event_count_bias",
    "micro_practice_count",
    "checkpoint",
    "exit_condition",
    "formal_creation_time",
]


def extract_teacher_text(markdown: str) -> str:
    parts = []
    pattern = re.compile(
        r"### Teacher-Facing Naturalized Text\s+(.*?)(?=\n### Leak Result|\n## Sample|\Z)",
        re.DOTALL,
    )
    for match in pattern.finditer(markdown):
        parts.append(match.group(1))
    return "\n".join(parts)


def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).is_file():
            failures.append(f"missing required file: {name}")

    for path in ROOT.iterdir():
        if path.is_file() and path.suffix.lower() == ".html":
            checks += 1
            failures.append(f"forbidden html artifact: {path.name}")

    sample_path = ROOT / "R224H_teacher_facing_naturalized_samples.md"
    if sample_path.is_file():
        teacher_text = extract_teacher_text(sample_path.read_text(encoding="utf-8"))
        checks += 1
        if not teacher_text.strip():
            failures.append("no teacher-facing naturalized text extracted")
        for token in FORBIDDEN_TOKENS:
            checks += 1
            if token in teacher_text:
                failures.append(f"forbidden token leaked in teacher-facing text: {token}")
        for phrase in [
            "本课不急着让学生完成复杂剪纸作品",
            "本课主要保护学生综合创作时间",
            "本课重点不是马上做一件作品",
        ]:
            checks += 1
            if phrase not in teacher_text:
                failures.append(f"missing allowed naturalized phrase: {phrase}")

    matrix_path = ROOT / "R224H_forbidden_token_scan_matrix.json"
    if matrix_path.is_file():
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        checks += 1
        if matrix.get("summary", {}).get("forbidden_token_leak_count") != 0:
            failures.append("forbidden_token_leak_count must be 0")
        checks += 1
        if matrix.get("summary", {}).get("all_samples_pass") is not True:
            failures.append("all_samples_pass must be true")
        checks += 1
        if matrix.get("summary", {}).get("decision") != "PASS_STATIC_LEAKAGE_PRECHECK":
            failures.append("matrix decision mismatch")
        samples = matrix.get("samples", [])
        checks += 1
        if len(samples) != 3:
            failures.append("expected 3 samples in scan matrix")
        for sample in samples:
            sid = sample.get("sample_id", "<missing>")
            checks += 1
            if sample.get("leak_pass") is not True:
                failures.append(f"{sid} leak_pass must be true")
            checks += 1
            if sample.get("forbidden_token_hits") != []:
                failures.append(f"{sid} forbidden_token_hits must be empty")
            checks += 1
            if sample.get("allowed_paraphrase_check") is not True:
                failures.append(f"{sid} allowed_paraphrase_check must be true")

    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.glob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json"}
    )
    for phrase in [
        "PASS_STATIC_LEAKAGE_PRECHECK",
        "review_ledger_trace_retained = true",
        "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
        "No HTML",
        "No R97B",
        "No runtime/provider/model",
        "No prompt change",
        "No v0.2 publication",
    ]:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing phrase: {phrase}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for key, expected in {
            "github_uploaded": False,
            "creates_new_html_page": False,
            "decision_target": "PASS_STATIC_LEAKAGE_PRECHECK",
        }.items():
            checks += 1
            if manifest.get(key) != expected:
                failures.append(f"manifest mismatch: {key}")
        for token in FORBIDDEN_TOKENS:
            checks += 1
            if token not in manifest.get("forbidden_tokens", []):
                failures.append(f"manifest missing forbidden token: {token}")
        for key, expected in {
            "modifies_r97b": False,
            "adds_route": False,
            "modifies_frontend_backend": False,
            "uses_runtime": False,
            "uses_provider_model": False,
            "changes_prompt": False,
            "uses_database": False,
            "lesson_body_writeback": False,
            "modifies_r223m_n_o_teacher_manuscripts": False,
            "modifies_r222d_component_library": False,
            "publishes_v0_2": False,
            "creates_html_page": False,
            "formal_apply": False,
        }.items():
            checks += 1
            if manifest.get("boundaries", {}).get(key) is not expected:
                failures.append(f"manifest boundary mismatch: {key}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_STATIC_LEAKAGE_PRECHECK" if not failures else "HOLD_TEACHER_DEFAULT_LEAKAGE_FOUND",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
