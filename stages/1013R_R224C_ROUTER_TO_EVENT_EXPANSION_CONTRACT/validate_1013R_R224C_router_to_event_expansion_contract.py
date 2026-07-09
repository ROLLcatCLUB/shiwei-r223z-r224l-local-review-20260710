import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224C_validator_result.json"


REQUIRED_FILES = [
    "R224C_router_to_event_expansion_contract.md",
    "R224C_router_output_to_event_field_mapping.json",
    "R224C_router_effect_on_teacher_manuscript_rules.md",
    "R224C_router_effect_on_review_ledger_rules.md",
    "R224C_router_effect_on_screen_sheet_evidence_rules.md",
    "R224C_event_density_rules_by_unit_phase_role.md",
    "R224C_three_sample_contract_trace.md",
    "R224C_risk_and_misuse_notes.md",
    "R224C_decision_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]


UNIT_PHASE_ROLES = [
    "intro_understanding",
    "technique_preparation",
    "practice_creation",
    "showcase_evaluation",
    "transfer_closure",
    "project_synthesis",
]


ROUTER_FIELDS = [
    "lesson_position_in_unit",
    "unit_phase_role",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
    "router_effect",
]


EVENT_FIELDS = [
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

    for role in UNIT_PHASE_ROLES:
        checks += 1
        if role not in combined:
            failures.append(f"missing unit_phase_role: {role}")

    mapping_path = ROOT / "R224C_router_output_to_event_field_mapping.json"
    if mapping_path.is_file():
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        for field in ROUTER_FIELDS:
            checks += 1
            if field not in mapping.get("router_fields", []):
                failures.append(f"mapping missing router field: {field}")
        event_map = mapping.get("classroom_event_expansion_fields", {})
        for field in EVENT_FIELDS:
            checks += 1
            if field not in event_map:
                failures.append(f"mapping missing event field: {field}")
        role_rules = mapping.get("unit_phase_role_rules", {})
        for role in UNIT_PHASE_ROLES:
            checks += 1
            if role not in role_rules:
                failures.append(f"mapping missing role rule: {role}")
        for boundary, expected in {
            "modifies_r223m_n_o_teacher_manuscripts": False,
            "publishes_v0_2": False,
            "creates_html_page": False,
            "modifies_r97b": False,
            "uses_runtime": False,
            "uses_provider_model": False,
            "changes_prompt": False,
            "uses_database": False,
            "formal_apply": False,
        }.items():
            checks += 1
            if mapping.get("boundaries", {}).get(boundary) is not expected:
                failures.append(f"mapping boundary mismatch: {boundary}")

    for phrase in [
        "Teacher default manuscript must not display",
        "Review ledger must preserve router fields",
        "Router output must change screen, learning sheet, and evidence expectations",
        "High support does not mean high whole-class explanation",
        "Low practice does not mean low teaching value",
        "PASS_CONTINUE_TO_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING",
    ]:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing phrase: {phrase}")

    for field in ROUTER_FIELDS:
        checks += 1
        if field not in combined:
            failures.append(f"combined docs missing router field: {field}")
    for field in EVENT_FIELDS:
        checks += 1
        if field not in combined:
            failures.append(f"combined docs missing event field: {field}")

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
        "decision": "PASS_CONTINUE_TO_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
