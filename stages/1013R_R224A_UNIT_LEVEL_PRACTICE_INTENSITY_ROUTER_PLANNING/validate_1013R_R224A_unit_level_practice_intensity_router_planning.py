import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224A_validator_result.json"


REQUIRED_FILES = [
    "R224A_unit_lesson_practice_intensity_router_contract.md",
    "R224A_router_schema_v0_1.json",
    "R224A_unit_phase_role_registry.md",
    "R224A_practice_intensity_decision_rules.md",
    "R224A_student_work_time_ratio_rules.md",
    "R224A_teacher_support_density_rules.md",
    "R224A_performance_task_and_stage_evidence_link_rules.md",
    "R224A_router_effect_on_classroom_event_expansion.md",
    "R224A_three_sample_router_fixture.md",
    "R224A_risk_and_misuse_notes.md",
    "R224A_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]


REQUIRED_SCHEMA_FIELDS = [
    "lesson_position_in_unit",
    "unit_phase_role",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
    "router_effect",
]


EXPECTED_SAMPLE_VALUES = {
    "M_stationery": {
        "lesson_position_in_unit": "late",
        "unit_phase_role": "practice_creation",
        "practice_intensity": "high",
        "student_work_time_ratio": "high",
        "teacher_support_density": "heavy",
    },
    "N_paper_print": {
        "lesson_position_in_unit": "middle",
        "unit_phase_role": "technique_preparation",
        "practice_intensity": "medium",
        "student_work_time_ratio": "medium",
        "teacher_support_density": "normal",
    },
    "O_color_collision": {
        "lesson_position_in_unit": "early",
        "unit_phase_role": "intro_understanding",
        "practice_intensity": "medium",
        "student_work_time_ratio": "medium",
        "teacher_support_density": "normal",
    },
}


REQUIRED_EFFECT_FIELDS = [
    "explanation_density",
    "demonstration_density",
    "micro_practice_count",
    "formal_creation_time",
    "teacher_circulation_focus",
    "showcase_evaluation_intensity",
    "learning_sheet_fields",
    "evidence_collection_mode",
]


def add_failure(failures, message):
    failures.append(message)


def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")


def extract_json_blocks(markdown_text):
    blocks = []
    for match in re.finditer(r"```json\s*(.*?)\s*```", markdown_text, re.DOTALL):
        blocks.append(json.loads(match.group(1)))
    return blocks


def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).is_file():
            add_failure(failures, f"missing required file: {name}")

    for path in ROOT.iterdir():
        if path.is_file() and path.suffix.lower() == ".html":
            checks += 1
            add_failure(failures, f"forbidden html artifact: {path.name}")

    schema_path = ROOT / "R224A_router_schema_v0_1.json"
    if schema_path.is_file():
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        for field in REQUIRED_SCHEMA_FIELDS:
            checks += 1
            if field not in schema.get("required_fields", []):
                add_failure(failures, f"schema missing required field: {field}")
        for enum_name, values in {
            "lesson_position_in_unit": ["early", "middle", "late", "final"],
            "unit_phase_role": [
                "intro_understanding",
                "technique_preparation",
                "practice_creation",
                "showcase_evaluation",
                "transfer_closure",
                "project_synthesis",
            ],
            "practice_intensity": ["low", "medium", "high"],
            "student_work_time_ratio": ["low", "medium", "high"],
            "teacher_support_density": ["light", "normal", "heavy"],
        }.items():
            for value in values:
                checks += 1
                if value not in schema.get("enums", {}).get(enum_name, []):
                    add_failure(failures, f"schema enum {enum_name} missing {value}")
        for boundary, expected in {
            "planning_only": True,
            "creates_new_teacher_manuscript": False,
            "modifies_r223m_n_o": False,
            "publishes_v0_2": False,
            "uses_runtime": False,
            "uses_provider_model": False,
            "changes_prompt": False,
            "uses_database": False,
            "creates_html_page": False,
            "formal_apply": False,
        }.items():
            checks += 1
            if schema.get("boundaries", {}).get(boundary) is not expected:
                add_failure(failures, f"schema boundary mismatch: {boundary}")

    fixture_path = ROOT / "R224A_three_sample_router_fixture.md"
    if fixture_path.is_file():
        fixtures = extract_json_blocks(fixture_path.read_text(encoding="utf-8"))
        checks += 1
        if len(fixtures) != 3:
            add_failure(failures, f"expected 3 fixture json blocks, got {len(fixtures)}")
        by_id = {fixture.get("sample_id"): fixture for fixture in fixtures}
        for sample_id, expected_values in EXPECTED_SAMPLE_VALUES.items():
            checks += 1
            if sample_id not in by_id:
                add_failure(failures, f"missing sample fixture: {sample_id}")
                continue
            fixture = by_id[sample_id]
            for key, expected in expected_values.items():
                checks += 1
                if fixture.get(key) != expected:
                    add_failure(failures, f"{sample_id} mismatch {key}: {fixture.get(key)} != {expected}")
            for field in ["performance_task_link", "stage_evidence_link", "router_effect"]:
                checks += 1
                if field not in fixture:
                    add_failure(failures, f"{sample_id} missing {field}")
            for field in REQUIRED_EFFECT_FIELDS:
                checks += 1
                if field not in fixture.get("router_effect", {}):
                    add_failure(failures, f"{sample_id} router_effect missing {field}")

    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.glob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json"}
    )
    for phrase in [
        "R224A = PLANNING_CONTRACT_ONLY",
        "PASS_CONTINUE_TO_R224B_ROUTER_FIXTURE_AND_REGRESSION",
        "No R97B",
        "No HTML",
        "not produce one universal fixed classroom pattern",
        "Do not infer high practice merely because the subject is art",
    ]:
        checks += 1
        if phrase not in combined:
            add_failure(failures, f"missing policy phrase: {phrase}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("github_uploaded") is not False:
            add_failure(failures, "manifest github_uploaded must be false")
        checks += 1
        if manifest.get("creates_new_html_page") is not False:
            add_failure(failures, "manifest creates_new_html_page must be false")
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
                add_failure(failures, f"manifest boundary mismatch: {key}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R224B_ROUTER_FIXTURE_AND_REGRESSION" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
