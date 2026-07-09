import json
from pathlib import Path


STAGE_ID = "1013R_R224L_R223M_STANDARD_V0_2_RELEASE_CANDIDATE_DRAFT_NON_APPLY"
ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
    "R224L_release_candidate_draft.md",
    "R224L_candidate_field_contract.json",
    "R224L_non_apply_and_non_publication_notice.md",
    "R224L_evidence_index_R224E_to_R224K.md",
    "R224L_teacher_default_and_review_ledger_rules.md",
    "R224L_boundary_check.md",
    "R224L_validator_result.json",
    "validate_1013R_R224L_release_candidate_draft_non_apply.py",
]

REQUIRED_EVIDENCE_STAGES = ["R224E", "R224F", "R224G", "R224H", "R224I", "R224J", "R224K"]
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
contract = load_json("R224L_candidate_field_contract.json")

add_check("manifest_stage_id", manifest.get("stage_id") == STAGE_ID)
add_check("contract_stage_id", contract.get("stage_id") == STAGE_ID)
add_check("manifest_decision", manifest.get("decision") == "PASS_LOCAL_RELEASE_CANDIDATE_DRAFT_NON_APPLY")
add_check("manifest_release_candidate_created", manifest.get("r223m_standard_v0_2_release_candidate_draft_created") is True)
add_check("contract_release_candidate_draft", contract.get("standard_candidate") == "R223M_STANDARD_V0_2_RELEASE_CANDIDATE_DRAFT")

for doc_name, doc in [("manifest", manifest), ("contract", contract)]:
    add_check(f"{doc_name}::v0_2_not_published", doc.get("r223m_standard_v0_2_published", doc.get("published")) is False)
    add_check(f"{doc_name}::formal_apply_false", doc.get("formal_apply_allowed") is False)

add_check("manifest_direct_publish_false", manifest.get("direct_publish_allowed") is False)
add_check("manifest_html_files_disallowed", manifest.get("html_files_allowed") is False)
add_check("manifest_teacher_manuscript_modification_disallowed", manifest.get("teacher_manuscript_modification_allowed") is False)
add_check("manifest_runtime_integration_disallowed", manifest.get("runtime_integration_allowed") is False)

for key, value in manifest.get("boundaries", {}).items():
    add_check(f"boundary_false::{key}", value is False)

manifest_stages = set(manifest.get("source_evidence_stages", []))
for stage in REQUIRED_EVIDENCE_STAGES:
    add_check(f"manifest_evidence_stage::{stage}", stage in manifest_stages)

manifest_fields = set(manifest.get("locked_router_input_fields", []))
contract_fields = {item.get("field") for item in contract.get("locked_router_input_fields", [])}
for field in REQUIRED_ROUTER_INPUT_FIELDS:
    add_check(f"manifest_router_input_field::{field}", field in manifest_fields)
    add_check(f"contract_router_input_field::{field}", field in contract_fields)

for item in contract.get("locked_router_input_fields", []):
    field = item.get("field", "UNKNOWN")
    add_check(f"contract::{field}::required_in_candidate", item.get("required_in_candidate") is True)
    add_check(f"contract::{field}::teacher_default_hidden", item.get("teacher_default_visible") is False)

manifest_bridge_fields = set(manifest.get("router_effect_bridge_fields", []))
contract_bridge_fields = {item.get("field") for item in contract.get("router_effect_bridge_fields", [])}
for field in REQUIRED_BRIDGE_FIELDS:
    add_check(f"manifest_bridge_field::{field}", field in manifest_bridge_fields)
    add_check(f"contract_bridge_field::{field}", field in contract_bridge_fields)

for item in contract.get("router_effect_bridge_fields", []):
    field = item.get("field", "UNKNOWN")
    add_check(f"contract_bridge::{field}::not_required_schema_object", item.get("required_schema_object_field") is False)

for doc_name, policy in [
    ("manifest", manifest.get("router_effect_policy", {})),
    ("contract", contract.get("router_effect_policy", {})),
]:
    add_check(f"{doc_name}::router_effect_not_required_schema_object", policy.get("required_schema_object") is False)
    add_check(f"{doc_name}::router_effect_computed_output", policy.get("computed_contract_output") is True)
    add_check(f"{doc_name}::review_ledger_summary", policy.get("review_ledger_summary") is True)
    add_check(f"{doc_name}::classroom_event_expansion_bridge", policy.get("classroom_event_expansion_bridge") is True)
    add_check(f"{doc_name}::teacher_raw_fields_hidden", policy.get("teacher_default_visible_raw_fields") is False)

visibility = contract.get("visibility_rules", {})
add_check("visibility_teacher_default_raw_hidden", visibility.get("teacher_default_raw_router_fields_visible") is False)
add_check("visibility_review_ledger_raw_visible", visibility.get("review_ledger_raw_router_fields_visible") is True)
add_check("visibility_naturalized_language_required", visibility.get("teacher_default_requires_naturalized_language") is True)

publication = contract.get("publication_rules", {})
add_check("publication_contract_v0_2_not_published", publication.get("r223m_standard_v0_2_published") is False)
add_check("publication_release_candidate_created", publication.get("release_candidate_draft_created") is True)
add_check("publication_direct_publish_false", publication.get("direct_publish_allowed") is False)
add_check("publication_explicit_authorization_required", publication.get("explicit_authorization_required_for_publication") is True)

markdown_text = "\n".join(p.read_text(encoding="utf-8") for p in ROOT.glob("*.md"))
required_phrases = [
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "formal_apply_allowed = false",
    "No HTML",
    "No R97B",
    "No runtime/provider/model",
    "No formal apply",
    "No v0.2 publication",
]
for phrase in required_phrases:
    add_check(f"required_phrase_present::{phrase}", phrase in markdown_text)

blocked_phrases = [
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "formal_apply_allowed = true",
    "direct_publish_allowed = true",
    "lesson body writeback allowed",
    "runtime integration allowed",
]
for phrase in blocked_phrases:
    add_check(f"blocked_phrase_absent::{phrase}", phrase not in markdown_text)

failed = [check for check in checks if not check["passed"]]
result = {
    "stage_id": STAGE_ID,
    "passed": not failed,
    "decision": "PASS_LOCAL_RELEASE_CANDIDATE_DRAFT_NON_APPLY" if not failed else "HOLD_RELEASE_CANDIDATE_DRAFT_RISK_FOUND",
    "check_count": len(checks),
    "failed_count": len(failed),
    "failed": failed,
    "checks": checks,
}

(ROOT / "R224L_validator_result.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps({
    "passed": result["passed"],
    "decision": result["decision"],
    "check_count": result["check_count"],
    "failed_count": result["failed_count"],
}, ensure_ascii=False, indent=2))

