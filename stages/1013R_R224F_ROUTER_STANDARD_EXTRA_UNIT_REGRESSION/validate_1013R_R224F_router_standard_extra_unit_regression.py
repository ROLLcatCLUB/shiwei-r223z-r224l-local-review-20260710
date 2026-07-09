import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224F_validator_result.json"


REQUIRED_FILES = [
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
    "R224F_extra_unit_regression_report.md",
    "R224F_sample_route_matrix.json",
    "R224F_teacher_visibility_leak_check.md",
    "R224F_review_ledger_trace_check.md",
]


REQUIRED_SAMPLE_TYPES = {
    "technique_preparation_unit",
    "project_synthesis_unit",
    "appreciation_intro_understanding_unit",
}


ROUTER_INPUT_FIELDS = [
    "unit_phase_role",
    "lesson_position_in_unit",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
]


ROUTER_EFFECT_FIELDS = [
    "event_count_bias",
    "explanation_density",
    "demonstration_density",
    "micro_practice_count",
    "formal_creation_time",
    "teacher_circulation_focus",
    "showcase_evaluation_intensity",
    "learning_sheet_fields",
    "evidence_collection_mode",
    "checkpoint",
    "exit_condition",
]


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

    matrix_path = ROOT / "R224F_sample_route_matrix.json"
    if matrix_path.is_file():
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        samples = matrix.get("samples", [])
        checks += 1
        if len(samples) < 3:
            failures.append("expected at least 3 samples")

        sample_types = {sample.get("unit_structure_type") for sample in samples}
        checks += 1
        if not REQUIRED_SAMPLE_TYPES.issubset(sample_types):
            failures.append(f"missing required sample types: {REQUIRED_SAMPLE_TYPES - sample_types}")

        for sample in samples:
            sid = sample.get("sample_id", "<missing>")
            router = sample.get("router_input_values", {})
            effect = sample.get("router_effect_summary", {})
            for field in ROUTER_INPUT_FIELDS:
                checks += 1
                if field not in router:
                    failures.append(f"{sid} missing router input field: {field}")
            for field in ROUTER_EFFECT_FIELDS:
                checks += 1
                if field not in effect:
                    failures.append(f"{sid} missing router effect field: {field}")
            trace = sample.get("review_ledger_trace", {})
            for field in ["source_status", "assumption_status", "confidence"]:
                checks += 1
                if field not in trace:
                    failures.append(f"{sid} missing review ledger trace field: {field}")
            checks += 1
            if sample.get("expected_teacher_default_effect", "").strip() == "":
                failures.append(f"{sid} missing expected teacher default effect")

        assertions = matrix.get("global_assertions", {})
        for key, expected in {
            "router_input_fields_reuse_r223p5": True,
            "router_effect_required_schema_object": False,
            "teacher_default_raw_router_field_visible": False,
            "review_ledger_trace_required": True,
            "samples_cover_technique_project_intro": True,
            "v0_2_published": False,
            "creates_html_page": False,
        }.items():
            checks += 1
            if assertions.get(key) is not expected:
                failures.append(f"global assertion mismatch: {key}")

    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.glob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json"}
    )

    for phrase in [
        "router_effect_required_schema_object = false",
        "teacher_visibility_leak = false",
        "review_ledger_trace = pass",
        "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
        "No HTML",
        "No R97B",
        "No runtime/provider/model",
        "PASS_CONTINUE_TO_R224G_ROUTER_STANDARD_REGRESSION_SUMMARY_OR_HOLD",
    ]:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing phrase: {phrase}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("github_uploaded") is not False:
            failures.append("manifest github_uploaded must be false")
        checks += 1
        if manifest.get("creates_new_html_page") is not False:
            failures.append("manifest creates_new_html_page must be false")
        checks += 1
        if not REQUIRED_SAMPLE_TYPES.issubset(set(manifest.get("covered_sample_types", []))):
            failures.append("manifest missing covered sample types")
        for field in ROUTER_INPUT_FIELDS:
            checks += 1
            if field not in manifest.get("required_router_input_fields", []):
                failures.append(f"manifest missing router input field: {field}")
        for field in ROUTER_EFFECT_FIELDS:
            checks += 1
            if field not in manifest.get("required_router_effect_fields", []):
                failures.append(f"manifest missing router effect field: {field}")
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
        "decision": "PASS_CONTINUE_TO_R224G_ROUTER_STANDARD_REGRESSION_SUMMARY_OR_HOLD" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
