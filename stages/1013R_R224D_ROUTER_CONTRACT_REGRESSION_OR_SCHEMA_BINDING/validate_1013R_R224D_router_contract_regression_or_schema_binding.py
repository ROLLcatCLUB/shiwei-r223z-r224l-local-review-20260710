import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224D_validator_result.json"


REQUIRED_FILES = [
    "R224D_router_contract_schema_binding_check.md",
    "R224D_field_overlap_with_R223P5_v0_2_candidate.md",
    "R224D_router_effect_object_policy.md",
    "R224D_teacher_default_visibility_guard.md",
    "R224D_review_ledger_router_trace_policy.md",
    "R224D_three_sample_binding_regression.md",
    "R224D_schema_delta_recommendation.md",
    "R224D_risk_and_conflict_notes.md",
    "R224D_decision_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]


EXISTING_REUSED = [
    "unit_phase_role",
    "lesson_position_in_unit",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
    "checkpoint",
    "exit_condition",
    "learning_sheet_fields",
]


DERIVED_FIELDS = [
    "router_effect",
    "event_count_bias",
    "explanation_density",
    "demonstration_density",
    "micro_practice_count",
    "formal_creation_time",
    "teacher_circulation_focus",
    "showcase_evaluation_intensity",
    "evidence_collection_mode",
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

    for field in EXISTING_REUSED:
        checks += 1
        if field not in combined:
            failures.append(f"missing reused field: {field}")

    for field in DERIVED_FIELDS:
        checks += 1
        if field not in combined:
            failures.append(f"missing derived field: {field}")

    for phrase in [
        "R224C router contract = compatible_with_R223P_5_v0_2_candidate",
        "router_effect should not become a single required object",
        "Do not publish a new schema version from R224D",
        "Teacher default manuscript must not display",
        "Review ledger can and should preserve router fields",
        "three_sample_binding_regression = PASS",
        "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
        "PASS_CONTINUE_TO_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK",
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
        binding = manifest.get("binding_decision", {})
        for key, expected in {
            "r224c_compatible_with_r223p5": True,
            "router_input_fields_already_covered": True,
            "router_effect_required_object": False,
            "v0_2_published": False,
        }.items():
            checks += 1
            if binding.get(key) is not expected:
                failures.append(f"binding decision mismatch: {key}")
        for field in EXISTING_REUSED:
            checks += 1
            if field not in manifest.get("existing_r223p5_fields_reused", []):
                failures.append(f"manifest missing reused field: {field}")
        for field in DERIVED_FIELDS:
            checks += 1
            if field not in manifest.get("derived_or_optional_effect_fields", []):
                failures.append(f"manifest missing derived field: {field}")
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
        "decision": "PASS_CONTINUE_TO_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
