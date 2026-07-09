import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224E_validator_result.json"


REQUIRED_FILES = [
    "R224E_unit_router_standard_candidate_lock_report.md",
    "R224E_unit_lesson_practice_intensity_router_schema_candidate.json",
    "R224E_router_input_field_policy.md",
    "R224E_router_effect_computed_output_policy.md",
    "R224E_router_to_event_expansion_binding_summary.md",
    "R224E_teacher_default_visibility_policy.md",
    "R224E_review_ledger_trace_policy.md",
    "R224E_three_sample_regression_summary.md",
    "R224E_usage_boundary_and_not_publish_notice.md",
    "R224E_next_stage_handoff.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]


ROUTER_INPUT_FIELDS = [
    "unit_phase_role",
    "lesson_position_in_unit",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
]


EVENT_FIELDS = [
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

    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.glob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json"}
    )

    for field in ROUTER_INPUT_FIELDS:
        checks += 1
        if field not in combined:
            failures.append(f"missing router input field: {field}")
    for field in EVENT_FIELDS:
        checks += 1
        if field not in combined:
            failures.append(f"missing affected event field: {field}")

    for phrase in [
        "PASS_LOCK_UNIT_ROUTER_STANDARD_CANDIDATE",
        "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
        "formal_standard_release\": false",
        "required_schema_object\": false",
        "computed_contract_output",
        "review_ledger_summary",
        "Teacher default manuscript must not display raw router",
        "Review ledger must preserve router trace",
        "No R97B",
        "No HTML",
    ]:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing phrase: {phrase}")

    schema_path = ROOT / "R224E_unit_lesson_practice_intensity_router_schema_candidate.json"
    if schema_path.is_file():
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        checks += 1
        if schema.get("formal_standard_release") is not False:
            failures.append("schema formal_standard_release must be false")
        checks += 1
        if schema.get("r223m_standard_v0_2_published") is not False:
            failures.append("schema r223m_standard_v0_2_published must be false")
        for field in ROUTER_INPUT_FIELDS:
            checks += 1
            if field not in schema.get("router_input_fields", {}).get("fields", {}):
                failures.append(f"schema missing router input field: {field}")
        effect = schema.get("router_effect_policy", {})
        for key, expected in {
            "required_schema_object": False,
            "computed_contract_output": True,
            "review_ledger_summary_allowed": True,
        }.items():
            checks += 1
            if effect.get(key) is not expected:
                failures.append(f"schema router_effect_policy mismatch: {key}")
        for field in EVENT_FIELDS:
            checks += 1
            if field not in effect.get("maps_to_classroom_event_expansion_fields", []):
                failures.append(f"schema router_effect missing event field: {field}")
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
            if schema.get("boundaries", {}).get(key) is not expected:
                failures.append(f"schema boundary mismatch: {key}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for key, expected in {
            "github_uploaded": False,
            "creates_new_html_page": False,
            "candidate_lock": True,
            "formal_standard_release": False,
            "r223m_standard_v0_2_published": False,
        }.items():
            checks += 1
            if manifest.get(key) is not expected:
                failures.append(f"manifest mismatch: {key}")
        for field in ROUTER_INPUT_FIELDS:
            checks += 1
            if field not in manifest.get("locked_router_input_fields", []):
                failures.append(f"manifest missing router input field: {field}")
        for field in EVENT_FIELDS:
            checks += 1
            if field not in manifest.get("affected_event_expansion_fields", []):
                failures.append(f"manifest missing affected event field: {field}")
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
        "decision": "PASS_LOCK_UNIT_ROUTER_STANDARD_CANDIDATE" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
