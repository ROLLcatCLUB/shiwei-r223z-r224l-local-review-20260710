# README FOR GPT REVIEW

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING
package_type: router_contract_schema_binding_check

## Review Purpose

R224D checks whether the R224C router-to-event expansion contract can bind to the R223P-5 v0.2 candidate schema without field conflict or premature publication.

It does not publish v0.2, does not edit R223M/N/O teacher manuscripts, does not create HTML, and does not start UI/R97B/runtime/model/prompt/db work.

## Key Files

- R224D_router_contract_schema_binding_check.md
- R224D_field_overlap_with_R223P5_v0_2_candidate.md
- R224D_router_effect_object_policy.md
- R224D_teacher_default_visibility_guard.md
- R224D_review_ledger_router_trace_policy.md
- R224D_three_sample_binding_regression.md
- R224D_schema_delta_recommendation.md
- R224D_risk_and_conflict_notes.md
- R224D_decision_report.md

## Review Questions

1. Are R224C router fields already covered by R223P-5?
2. Which fields are existing schema fields?
3. Which fields are derived effects rather than schema fields?
4. Should `router_effect` stay computed rather than required?
5. Are teacher default visibility guards clear?
6. Can review ledger preserve router trace with source/assumption status?
7. Do the three samples regress cleanly?
8. Is v0.2 still not published?

## Decision Options

```text
A. PASS_CONTINUE_TO_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK
B. HOLD_FOR_ROUTER_SCHEMA_BINDING_REWORK
C. HOLD_FOR_R223P_V0_2_FIELD_CONFLICT_RECHECK
```
