import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "R224G_validator_result.json"


REQUIRED_FILES = [
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
    "R224G_regression_summary_report.md",
    "R224G_r224e_r224f_coverage_matrix.json",
    "R224G_publication_hold_rationale.md",
    "R224G_next_stage_options.md",
]


REQUIRED_PHRASES = [
    "PASS_SUMMARY_READY_AND_HOLD_PUBLICATION",
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "router input fields reuse R223P-5",
    "router_effect is not a required schema object",
    "teacher default manuscript does not display raw router fields",
    "review ledger preserves router trace",
    "teacher default manuscript leakage regression",
    "classroom_event_expansion formal field convergence",
    "No HTML",
    "No R97B",
    "No runtime/provider/model",
    "No v0.2 publication"
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

    for phrase in REQUIRED_PHRASES:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing phrase: {phrase}")

    matrix_path = ROOT / "R224G_r224e_r224f_coverage_matrix.json"
    if matrix_path.is_file():
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        checks += 1
        if matrix.get("decision") != "PASS_SUMMARY_READY_AND_HOLD_PUBLICATION":
            failures.append("matrix decision mismatch")
        checks += 1
        if matrix.get("r223m_standard_v0_2_published") is not False:
            failures.append("matrix v0_2 published must be false")
        locked = matrix.get("r224e_locked_items", {})
        for key, expected in {
            "router_input_fields_reuse_r223p5": True,
            "router_effect_required_schema_object": False,
            "router_effect_computed_contract_output": True,
            "router_effect_review_ledger_summary": True,
            "teacher_default_hides_raw_router_fields": True,
            "review_ledger_preserves_router_trace": True,
            "v0_2_published": False,
        }.items():
            checks += 1
            if locked.get(key) is not expected:
                failures.append(f"R224E locked item mismatch: {key}")
        samples = matrix.get("r224f_extra_regression_samples", [])
        checks += 1
        if len(samples) != 3:
            failures.append("expected 3 R224F samples")
        sample_types = {sample.get("unit_structure_type") for sample in samples}
        for required in [
            "technique_preparation_unit",
            "project_synthesis_unit",
            "appreciation_intro_understanding_unit",
        ]:
            checks += 1
            if required not in sample_types:
                failures.append(f"missing sample type: {required}")
        not_covered = matrix.get("not_yet_covered_for_publication", {})
        for key in [
            "teacher_default_true_generation_leak_regression",
            "classroom_event_expansion_formal_field_convergence",
            "ui_or_r97b_readiness",
            "cross_grade_real_unit_pressure_test",
            "long_unit_short_unit_stress_test",
        ]:
            checks += 1
            if not_covered.get(key) is not False:
                failures.append(f"publication gap should remain false/not done: {key}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for key, expected in {
            "github_uploaded": False,
            "creates_new_html_page": False,
            "decision": "PASS_SUMMARY_READY_AND_HOLD_PUBLICATION",
            "r223m_standard_v0_2_published": False,
        }.items():
            checks += 1
            if manifest.get(key) != expected:
                failures.append(f"manifest mismatch: {key}")
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
        "decision": "PASS_SUMMARY_READY_AND_HOLD_PUBLICATION" if not failures else "FAIL",
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
