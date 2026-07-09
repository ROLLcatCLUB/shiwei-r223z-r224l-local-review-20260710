import json
from pathlib import Path


STAGE_ID = "1013R_R224J_CROSS_GRADE_AND_UNIT_LENGTH_PRESSURE_STATIC_REGRESSION"
ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
    "R224J_cross_grade_and_unit_length_pressure_report.md",
    "R224J_cross_grade_pressure_matrix.json",
    "R224J_unit_length_pressure_matrix.json",
    "R224J_teacher_default_visibility_check.md",
    "R224J_review_ledger_trace_check.md",
    "R224J_publication_status_notice.md",
    "R224J_validator_result.json",
    "validate_1013R_R224J_cross_grade_and_unit_length_pressure_static_regression.py",
]

REQUIRED_ROUTER_INPUT_FIELDS = [
    "unit_phase_role",
    "lesson_position_in_unit",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
]

REQUIRED_BRIDGE_FIELDS = [
    "event_count_bias",
    "observation_time_bias",
    "demonstration_time_bias",
    "micro_practice_count_bias",
    "formal_creation_time_bias",
    "teacher_support_density_hint",
    "checkpoint_density_hint",
    "exit_condition_hint",
]

REQUIRED_GRADE_BANDS = {"low", "middle", "high"}
REQUIRED_UNIT_LENGTH_TYPES = {
    "single_lesson_short_task",
    "two_lesson_progression",
    "multi_lesson_project",
}

checks = []


def add_check(name, passed, detail=""):
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def load_json(name):
    with (ROOT / name).open("r", encoding="utf-8") as f:
        return json.load(f)


for filename in REQUIRED_FILES:
    add_check(f"required_file_present::{filename}", (ROOT / filename).exists())

html_files = [p.name for p in ROOT.glob("*.html")]
add_check("no_html_files", len(html_files) == 0, ", ".join(html_files))

manifest = load_json("PACKAGE_MANIFEST.json")
cross_grade = load_json("R224J_cross_grade_pressure_matrix.json")
unit_length = load_json("R224J_unit_length_pressure_matrix.json")

for doc_name, doc in [
    ("manifest", manifest),
    ("cross_grade", cross_grade),
    ("unit_length", unit_length),
]:
    add_check(f"{doc_name}::stage_id", doc.get("stage_id") == STAGE_ID)
    add_check(f"{doc_name}::decision", doc.get("decision") == "PASS_CROSS_GRADE_AND_LENGTH_STATIC_REGRESSION")
    add_check(f"{doc_name}::v0_2_not_published", doc.get("r223m_standard_v0_2_published") is False)

add_check("manifest_router_effect_required_schema_object_false", manifest.get("router_effect_required_schema_object") is False)

for key, value in manifest.get("boundaries", {}).items():
    add_check(f"boundary_false::{key}", value is False)

for field in REQUIRED_ROUTER_INPUT_FIELDS:
    add_check(f"manifest_router_input_field::{field}", field in manifest.get("required_router_input_fields", []))

for field in REQUIRED_BRIDGE_FIELDS:
    add_check(f"manifest_bridge_field::{field}", field in manifest.get("required_router_effect_bridge_fields", []))


def validate_matrix(name, doc, required_grade_bands=None, required_unit_lengths=None):
    policy = doc.get("router_effect_policy", {})
    add_check(f"{name}::router_effect_not_required_schema_object", policy.get("required_schema_object") is False)
    add_check(f"{name}::router_effect_computed_output", policy.get("computed_contract_output") is True)
    add_check(f"{name}::review_ledger_summary", policy.get("review_ledger_summary") is True)
    add_check(f"{name}::classroom_event_expansion_bridge", policy.get("classroom_event_expansion_bridge") is True)
    add_check(f"{name}::teacher_raw_fields_hidden", policy.get("teacher_default_visible_raw_fields") is False)

    for field in REQUIRED_ROUTER_INPUT_FIELDS:
        add_check(f"{name}::required_router_input_field::{field}", field in doc.get("required_router_input_fields", []))

    for field in REQUIRED_BRIDGE_FIELDS:
        add_check(f"{name}::required_bridge_field::{field}", field in doc.get("required_router_effect_bridge_fields", []))

    samples = doc.get("samples", [])
    add_check(f"{name}::sample_count_at_least_three", len(samples) >= 3)

    found_grade_bands = {sample.get("grade_band") for sample in samples}
    found_unit_lengths = {sample.get("unit_length_type") for sample in samples}

    if required_grade_bands:
        for grade_band in required_grade_bands:
            add_check(f"{name}::required_grade_band::{grade_band}", grade_band in found_grade_bands)

    if required_unit_lengths:
        for unit_length in required_unit_lengths:
            add_check(f"{name}::required_unit_length::{unit_length}", unit_length in found_unit_lengths)

    for sample in samples:
        sample_id = sample.get("sample_id", "UNKNOWN")
        add_check(f"{name}::{sample_id}::lesson_title_present", bool(sample.get("lesson_title")))
        add_check(f"{name}::{sample_id}::grade_band_present", sample.get("grade_band") in REQUIRED_GRADE_BANDS)
        add_check(f"{name}::{sample_id}::unit_length_type_present", sample.get("unit_length_type") in REQUIRED_UNIT_LENGTH_TYPES)
        add_check(f"{name}::{sample_id}::unit_structure_type_present", bool(sample.get("unit_structure_type")))

        router_inputs = sample.get("router_input_values", {})
        bridge = sample.get("computed_router_effect_summary", {})
        affected = sample.get("affected_classroom_event_expansion_fields", {})

        for field in REQUIRED_ROUTER_INPUT_FIELDS:
            add_check(f"{name}::{sample_id}::router_input::{field}", field in router_inputs and router_inputs.get(field) not in ("", None))
        for field in REQUIRED_BRIDGE_FIELDS:
            add_check(f"{name}::{sample_id}::bridge_field::{field}", field in bridge and bridge.get(field) not in ("", None))

        add_check(f"{name}::{sample_id}::affected_event_fields_present", len(affected) >= 4)
        add_check(f"{name}::{sample_id}::teacher_implication_present", bool(sample.get("teacher_facing_naturalized_implication")))
        add_check(f"{name}::{sample_id}::review_ledger_trace_retained", sample.get("review_ledger_retained_trace") is True)
        add_check(f"{name}::{sample_id}::required_schema_object_leak_false", sample.get("required_schema_object_leak") is False)
        add_check(f"{name}::{sample_id}::teacher_default_field_leak_false", sample.get("teacher_default_field_leak") is False)

    global_checks = doc.get("global_checks", {})
    for key in [
        "all_samples_have_grade_band",
        "all_samples_have_unit_length_type",
        "all_samples_have_router_inputs",
        "all_samples_have_router_effect_bridge_fields",
        "all_samples_have_teacher_naturalized_implication",
        "all_samples_have_review_ledger_trace",
    ]:
        add_check(f"{name}::global_true::{key}", global_checks.get(key) is True)

    for key in [
        "any_required_schema_object_leak",
        "any_teacher_default_field_leak",
    ]:
        add_check(f"{name}::global_false::{key}", global_checks.get(key) is False)


validate_matrix("cross_grade", cross_grade, required_grade_bands=REQUIRED_GRADE_BANDS)
validate_matrix("unit_length", unit_length, required_unit_lengths=REQUIRED_UNIT_LENGTH_TYPES)

markdown_text = "\n".join(p.read_text(encoding="utf-8") for p in ROOT.glob("*.md"))
blocked_phrases = [
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "formal_apply_allowed = true",
    "lesson_body_writeback = true",
    "router_effect_required_schema_object = true",
]
for phrase in blocked_phrases:
    add_check(f"blocked_phrase_absent::{phrase}", phrase not in markdown_text)

failed = [check for check in checks if not check["passed"]]
result = {
    "stage_id": STAGE_ID,
    "passed": not failed,
    "decision": "PASS_CROSS_GRADE_AND_LENGTH_STATIC_REGRESSION" if not failed else "HOLD_ROUTER_PRESSURE_RISK_FOUND",
    "check_count": len(checks),
    "failed_count": len(failed),
    "failed": failed,
    "checks": checks,
}

(ROOT / "R224J_validator_result.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps({
    "passed": result["passed"],
    "decision": result["decision"],
    "check_count": result["check_count"],
    "failed_count": result["failed_count"],
}, ensure_ascii=False, indent=2))

