import json
from pathlib import Path


STAGE_ID = "1013R_R224I_ROUTER_TO_CLASSROOM_EVENT_EXPANSION_FIELD_CONVERGENCE_STATIC_PRECHECK"
ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
    "R224I_field_convergence_static_precheck_report.md",
    "R224I_router_to_event_expansion_mapping_matrix.json",
    "R224I_required_schema_object_leak_check.md",
    "R224I_teacher_default_visibility_check.md",
    "R224I_review_ledger_trace_check.md",
    "R224I_publication_status_notice.md",
    "R224I_validator_result.json",
    "validate_1013R_R224I_router_to_classroom_event_expansion_field_convergence_static_precheck.py",
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

REQUIRED_SAMPLE_TYPES = {
    "technique_preparation_unit",
    "project_synthesis_unit",
    "appreciation_intro_understanding_unit",
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
matrix = load_json("R224I_router_to_event_expansion_mapping_matrix.json")

add_check("manifest_stage_id", manifest.get("stage_id") == STAGE_ID)
add_check("matrix_stage_id", matrix.get("stage_id") == STAGE_ID)
add_check("decision_pass", matrix.get("decision") == "PASS_FIELD_CONVERGENCE_STATIC_PRECHECK")
add_check("manifest_decision_pass", manifest.get("decision") == "PASS_FIELD_CONVERGENCE_STATIC_PRECHECK")
add_check("r223m_standard_v0_2_not_published", matrix.get("r223m_standard_v0_2_published") is False)
add_check("manifest_v0_2_not_published", manifest.get("r223m_standard_v0_2_published") is False)
add_check("router_effect_not_required_schema_object_matrix", matrix.get("router_effect_policy", {}).get("required_schema_object") is False)
add_check("router_effect_not_required_schema_object_manifest", manifest.get("router_effect_required_schema_object") is False)

manifest_boundaries = manifest.get("boundaries", {})
for key, value in manifest_boundaries.items():
    add_check(f"boundary_false::{key}", value is False)

manifest_input_fields = manifest.get("required_router_input_fields", [])
matrix_input_fields = matrix.get("router_input_field_policy", {}).get("fields", [])
for field in REQUIRED_ROUTER_INPUT_FIELDS:
    add_check(f"manifest_router_input_field::{field}", field in manifest_input_fields)
    add_check(f"matrix_router_input_field::{field}", field in matrix_input_fields)

manifest_bridge_fields = manifest.get("required_router_effect_bridge_fields", [])
matrix_targets = matrix.get("field_convergence_targets", [])
for field in REQUIRED_BRIDGE_FIELDS:
    add_check(f"manifest_bridge_field::{field}", field in manifest_bridge_fields)
    add_check(f"matrix_bridge_target::{field}", field in matrix_targets)

samples = matrix.get("samples", [])
add_check("sample_count_is_three", len(samples) == 3)
found_types = {sample.get("unit_structure_type") for sample in samples}
for sample_type in REQUIRED_SAMPLE_TYPES:
    add_check(f"required_sample_type::{sample_type}", sample_type in found_types)

for sample in samples:
    sample_id = sample.get("sample_id", "UNKNOWN")
    router_inputs = sample.get("router_input_values", {})
    bridge = sample.get("computed_router_effect_summary", {})
    affected = sample.get("affected_classroom_event_expansion_fields", {})

    for field in REQUIRED_ROUTER_INPUT_FIELDS:
        add_check(f"{sample_id}::router_input::{field}", field in router_inputs and router_inputs.get(field) not in ("", None))
    for field in REQUIRED_BRIDGE_FIELDS:
        add_check(f"{sample_id}::bridge_field::{field}", field in bridge and bridge.get(field) not in ("", None))

    add_check(f"{sample_id}::affected_event_fields_present", len(affected) >= 4)
    add_check(f"{sample_id}::teacher_implication_present", bool(sample.get("teacher_facing_naturalized_implication")))
    add_check(f"{sample_id}::review_ledger_trace_retained", sample.get("review_ledger_retained_trace") is True)
    add_check(f"{sample_id}::required_schema_object_leak_false", sample.get("required_schema_object_leak") is False)
    add_check(f"{sample_id}::teacher_default_field_leak_false", sample.get("teacher_default_field_leak") is False)

global_checks = matrix.get("global_checks", {})
for key in [
    "all_samples_have_router_inputs",
    "all_samples_have_router_effect_bridge_fields",
    "all_samples_have_teacher_naturalized_implication",
    "all_samples_have_review_ledger_trace",
]:
    add_check(f"global_true::{key}", global_checks.get(key) is True)

for key in [
    "any_required_schema_object_leak",
    "any_teacher_default_field_leak",
]:
    add_check(f"global_false::{key}", global_checks.get(key) is False)

markdown_text = "\n".join(
    p.read_text(encoding="utf-8") for p in ROOT.glob("*.md")
)
blocked_phrases = [
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "formal_apply_allowed = true",
    "lesson_body_writeback = true",
]
for phrase in blocked_phrases:
    add_check(f"blocked_phrase_absent::{phrase}", phrase not in markdown_text)

failed = [check for check in checks if not check["passed"]]
result = {
    "stage_id": STAGE_ID,
    "passed": not failed,
    "decision": "PASS_FIELD_CONVERGENCE_STATIC_PRECHECK" if not failed else "HOLD_FIELD_CONVERGENCE_RISK_FOUND",
    "check_count": len(checks),
    "failed_count": len(failed),
    "failed": failed,
    "checks": checks,
}

(ROOT / "R224I_validator_result.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps({
    "passed": result["passed"],
    "decision": result["decision"],
    "check_count": result["check_count"],
    "failed_count": result["failed_count"],
}, ensure_ascii=False, indent=2))

