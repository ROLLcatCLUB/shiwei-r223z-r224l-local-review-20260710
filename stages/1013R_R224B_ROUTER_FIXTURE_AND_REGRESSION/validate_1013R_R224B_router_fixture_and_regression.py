import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224B_validator_result.json"


REQUIRED_FILES = [
    "R224B_router_regression_plan.md",
    "R224B_router_schema_normalization_notes.md",
    "R224B_sample_M_stationery_router_expansion_fixture.md",
    "R224B_sample_N_paper_print_router_expansion_fixture.md",
    "R224B_sample_O_color_collision_router_expansion_fixture.md",
    "R224B_three_sample_router_regression_matrix.json",
    "R224B_density_effect_check.md",
    "R224B_teacher_default_view_impact_check.md",
    "R224B_review_ledger_impact_check.md",
    "R224B_risk_and_misuse_regression.md",
    "R224B_decision_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]


EXPECTED = {
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


EFFECT_FIELDS = [
    "explanation_density",
    "demonstration_density",
    "micro_practice_count",
    "formal_creation_time",
    "teacher_circulation_focus",
    "showcase_evaluation_intensity",
    "learning_sheet_fields",
    "evidence_collection_mode",
]


def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")


def extract_first_json_block(name):
    text = read_text(name)
    match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    if not match:
        raise ValueError(f"no json block in {name}")
    return json.loads(match.group(1))


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

    fixture_files = {
        "M_stationery": "R224B_sample_M_stationery_router_expansion_fixture.md",
        "N_paper_print": "R224B_sample_N_paper_print_router_expansion_fixture.md",
        "O_color_collision": "R224B_sample_O_color_collision_router_expansion_fixture.md",
    }

    fixture_profiles = {}
    for sample_id, filename in fixture_files.items():
        if (ROOT / filename).is_file():
            fixture = extract_first_json_block(filename)
            fixture_profiles[sample_id] = fixture
            checks += 1
            if fixture.get("sample_id") != sample_id:
                failures.append(f"{filename} sample_id mismatch")
            for key, expected in EXPECTED[sample_id].items():
                checks += 1
                if fixture.get(key) != expected:
                    failures.append(f"{sample_id} {key} mismatch: {fixture.get(key)} != {expected}")
            for key in ["performance_task_link", "stage_evidence_link", "router_effect"]:
                checks += 1
                if key not in fixture:
                    failures.append(f"{sample_id} missing {key}")
            for key in EFFECT_FIELDS:
                checks += 1
                if key not in fixture.get("router_effect", {}):
                    failures.append(f"{sample_id} router_effect missing {key}")

    matrix_path = ROOT / "R224B_three_sample_router_regression_matrix.json"
    if matrix_path.is_file():
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        samples = {item["sample_id"]: item for item in matrix.get("samples", [])}
        checks += 1
        if set(samples) != set(EXPECTED):
            failures.append(f"matrix sample ids mismatch: {set(samples)}")
        for sample_id, expected_values in EXPECTED.items():
            if sample_id in samples:
                router = samples[sample_id].get("router_values", {})
                for key, expected in expected_values.items():
                    checks += 1
                    if router.get(key) != expected:
                        failures.append(f"matrix {sample_id} {key} mismatch")
                checks += 1
                if samples[sample_id].get("teacher_default_view", {}).get("router_field_names_visible") is not False:
                    failures.append(f"matrix {sample_id} teacher default view must hide router field names")
                checks += 1
                if samples[sample_id].get("review_ledger", {}).get("router_fields_allowed") is not True:
                    failures.append(f"matrix {sample_id} review ledger must allow router fields")
        assertions = matrix.get("global_regression_assertions", {})
        for key in [
            "three_samples_have_complete_router_values",
            "density_effects_are_not_identical",
            "teacher_default_view_hides_router_field_names",
            "review_ledger_preserves_router_fields",
            "does_not_modify_existing_teacher_manuscripts",
            "does_not_publish_v0_2",
            "does_not_create_html",
        ]:
            checks += 1
            if assertions.get(key) is not True:
                failures.append(f"global assertion must be true: {key}")

    if set(fixture_profiles) == set(EXPECTED):
        checks += 1
        effect_tuples = {
            sample_id: (
                f["unit_phase_role"],
                f["practice_intensity"],
                f["student_work_time_ratio"],
                f["teacher_support_density"],
                f["router_effect"]["formal_creation_time"],
                f["router_effect"]["demonstration_density"],
            )
            for sample_id, f in fixture_profiles.items()
        }
        if len(set(effect_tuples.values())) != 3:
            failures.append("fixture density effects are not distinct across three samples")

    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.glob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json"}
    )
    for phrase in [
        "density_enum",
        "count_range",
        "density_or_strategy",
        "text_or_list",
        "Do not force every `router_effect` value into low / medium / high",
        "Teacher default view should not display",
        "Review ledger may preserve router fields",
        "PASS_CONTINUE_TO_R224C_ROUTER_TO_EVENT_EXPANSION_CONTRACT",
        "No HTML",
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
        "decision": "PASS_CONTINUE_TO_R224C_ROUTER_TO_EVENT_EXPANSION_CONTRACT" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
