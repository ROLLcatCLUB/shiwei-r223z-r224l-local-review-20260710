import json
from pathlib import Path


STAGE_ID = "1013R_R224K_ROUTER_STANDARD_PUBLICATION_READINESS_GATE_AND_HOLD"
ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
    "R224K_publication_readiness_gate_report.md",
    "R224K_e_to_j_evidence_chain_matrix.json",
    "R224K_remaining_risk_and_hold_rationale.md",
    "R224K_release_candidate_draft_readiness_notice.md",
    "R224K_boundary_check.md",
    "R224K_validator_result.json",
    "validate_1013R_R224K_router_standard_publication_readiness_gate_and_hold.py",
]

REQUIRED_STAGES = ["R224E", "R224F", "R224G", "R224H", "R224I", "R224J"]

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
matrix = load_json("R224K_e_to_j_evidence_chain_matrix.json")

add_check("manifest_stage_id", manifest.get("stage_id") == STAGE_ID)
add_check("matrix_stage_id", matrix.get("stage_id") == STAGE_ID)
add_check("manifest_decision", manifest.get("decision") == "PASS_PUBLICATION_READINESS_GATE_AND_HOLD_UNTIL_EXPLICIT_AUTHORIZATION")
add_check("matrix_decision", matrix.get("decision") == "PASS_PUBLICATION_READINESS_GATE_AND_HOLD_UNTIL_EXPLICIT_AUTHORIZATION")

for doc_name, doc in [("manifest", manifest), ("matrix", matrix)]:
    add_check(f"{doc_name}::publication_readiness_pass", doc.get("publication_readiness_summary") == "PASS")
    add_check(f"{doc_name}::publication_hold", doc.get("publication") == "HOLD")
    add_check(f"{doc_name}::v0_2_not_published", doc.get("r223m_standard_v0_2_published") is False)
    add_check(f"{doc_name}::direct_publish_forbidden", doc.get("direct_publish_allowed") is False)
    add_check(f"{doc_name}::release_candidate_draft_allowed_next", doc.get("release_candidate_draft_allowed_next") is True)

add_check("manifest_technical_blocker_false", manifest.get("technical_blocker_remaining") is False)
add_check("matrix_technical_blocker_false", matrix.get("hold_reason", {}).get("technical_blocker_remaining") is False)
add_check("matrix_explicit_authorization_required", matrix.get("hold_reason", {}).get("explicit_user_authorization_required") is True)

for key, value in manifest.get("boundaries", {}).items():
    add_check(f"boundary_false::{key}", value is False)

manifest_stages = set(manifest.get("evidence_stages", []))
matrix_stages = {item.get("stage") for item in matrix.get("evidence_chain", [])}
for stage in REQUIRED_STAGES:
    add_check(f"manifest_evidence_stage::{stage}", stage in manifest_stages)
    add_check(f"matrix_evidence_stage::{stage}", stage in matrix_stages)

chain = matrix.get("evidence_chain", [])
add_check("evidence_chain_count_is_six", len(chain) == 6)
for item in chain:
    stage = item.get("stage", "UNKNOWN")
    add_check(f"{stage}::status_pass", item.get("status") == "PASS")
    add_check(f"{stage}::decision_present", bool(item.get("decision")))
    add_check(f"{stage}::evidence_nonempty", len(item.get("evidence", [])) >= 3)
    add_check(f"{stage}::publication_impact_present", bool(item.get("publication_impact")))
    add_check(f"{stage}::risk_remaining_present", bool(item.get("risk_remaining")))

gate_answers = matrix.get("gate_answers", {})
for key in [
    "candidate_has_publication_readiness_summary",
    "publication_should_hold",
    "hold_reason_is_authorization_not_technical_gap",
    "release_candidate_draft_allowed",
    "direct_publish_forbidden",
]:
    add_check(f"gate_answer_true::{key}", gate_answers.get(key) is True)

markdown_text = "\n".join(p.read_text(encoding="utf-8") for p in ROOT.glob("*.md"))
required_phrases = [
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "PUBLICATION = HOLD",
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
    "PUBLICATION = PUBLISH",
    "direct_publish_allowed = true",
    "formal_apply_allowed = true",
    "lesson_body_writeback = true",
]
for phrase in blocked_phrases:
    add_check(f"blocked_phrase_absent::{phrase}", phrase not in markdown_text)

failed = [check for check in checks if not check["passed"]]
result = {
    "stage_id": STAGE_ID,
    "passed": not failed,
    "decision": "PASS_PUBLICATION_READINESS_GATE_AND_HOLD_UNTIL_EXPLICIT_AUTHORIZATION" if not failed else "HOLD_PUBLICATION_READINESS_GATE_RISK_FOUND",
    "check_count": len(checks),
    "failed_count": len(failed),
    "failed": failed,
    "checks": checks,
}

(ROOT / "R224K_validator_result.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps({
    "passed": result["passed"],
    "decision": result["decision"],
    "check_count": result["check_count"],
    "failed_count": result["failed_count"],
}, ensure_ascii=False, indent=2))

