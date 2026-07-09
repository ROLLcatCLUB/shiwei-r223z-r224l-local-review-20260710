import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R223Z_validator_result.json"


REQUIRED_FILES = [
    "R223Z_stage_closure_report.md",
    "R223Z_source_of_truth_index.md",
    "R223Z_deprecated_artifacts_and_do_not_use.md",
    "R223Z_line_routing_policy.md",
    "R223Z_v0_2_candidate_usage_policy.md",
    "R223Z_html_artifact_policy.md",
    "R223Z_next_stage_options.md",
    "R223Z_recommended_next_step.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]


REQUIRED_STATUS_PHRASES = [
    "R223M-P5 = GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0.1_LOCKED_AS_CANDIDATE",
    "R223N = PAPER_PRINT_CROSS_SAMPLE_VALIDATION_PASS",
    "R223O-P1 = COLOR_MANUSCRIPT_STRUCTURE_RECOVERY_PASS",
    "R223P-5 = PASS_LOCK_R223M_STANDARD_V0_2_CANDIDATE",
    "R223Q = PASS_TRUE_GENERATION_REGRESSION_GATE",
    "R223R = PASS_V0_2_CANDIDATE_PILOT_ROUTE_PLANNING",
    "R223S = PASS_OPT_IN_SANDBOX_ROUTE_SPEC",
    "R223T = PASS_FIXTURE_ONLY_SANDBOX_PREVIEW",
    "R223U = PASS_SANDBOX_TEACHER_REVIEW",
    "R223V = PASS_SANDBOX_REDUCTION_OR_PILOT_HOLD",
    "R223W = PASS_REVIEW_ONLY_PILOT_GATE_SPEC",
    "R223X-P1 = PASS_NON_VISUAL_REVIEW_GATE_PACKAGE",
    "R223Y = CANCELLED_OR_RESCOPED",
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
]


REQUIRED_SOURCE_FILES = [
    "R223M_P4_P1_teacher_readable_process_v6.html",
    "R223N_P3_P1_teacher_manuscript_draft_v5.html",
    "R223O_P1_teacher_manuscript_draft_v2.html",
]


REQUIRED_ROUTE_PHRASES = [
    "教师稿质量问题 -> R223M / R223N / R223O",
    "v0.2 字段 / schema / ledger 问题 -> R223P / R223Q",
    "sandbox / gate 审核问题 -> md / json / checklist / validator",
    "正式 UI / R97B 问题 -> BLOCKED until separately authorized",
]


FORBIDDEN_FILENAMES = [".html"]


def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).is_file():
            failures.append(f"missing required file: {name}")

    for path in ROOT.iterdir():
        if path.is_file() and path.name != RESULT.name:
            lower = path.name.lower()
            for forbidden in FORBIDDEN_FILENAMES:
                checks += 1
                if forbidden in lower:
                    failures.append(f"forbidden html artifact found: {path.name}")

    text_blob = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.glob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json"}
    )

    for phrase in REQUIRED_STATUS_PHRASES:
        checks += 1
        if phrase not in text_blob:
            failures.append(f"missing locked status phrase: {phrase}")

    for filename in REQUIRED_SOURCE_FILES:
        checks += 1
        if filename not in text_blob:
            failures.append(f"missing source of truth file: {filename}")

    for phrase in REQUIRED_ROUTE_PHRASES:
        checks += 1
        if phrase not in text_blob:
            failures.append(f"missing routing phrase: {phrase}")

    for phrase in [
        "HTML artifacts are allowed only in two cases",
        "R223X static HTML must not be used",
        "R224A_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING",
        "Do not open formal UI next",
    ]:
        checks += 1
        if phrase not in text_blob:
            failures.append(f"missing policy phrase: {phrase}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("github_uploaded") is not False:
            failures.append("manifest github_uploaded must be false")
        checks += 1
        if manifest.get("creates_new_html_page") is not False:
            failures.append("manifest creates_new_html_page must be false")
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
        "decision": "PASS_R223Z_STAGE_CLOSURE_AND_NEXT_PLANNING" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
