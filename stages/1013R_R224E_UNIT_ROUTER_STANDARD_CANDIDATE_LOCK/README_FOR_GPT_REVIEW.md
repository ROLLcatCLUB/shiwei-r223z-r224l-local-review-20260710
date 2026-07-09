# README FOR GPT REVIEW

stage_id: 1013R_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK
package_type: unit_router_standard_candidate_lock

## Review Purpose

R224E locks the unit lesson practice intensity router as a standard candidate.

It is a companion candidate for R223P-5 v0.2 candidate. It does not publish v0.2 and does not start UI, runtime, prompt, model, database, or R97B work.

## Key Files

- R224E_unit_router_standard_candidate_lock_report.md
- R224E_unit_lesson_practice_intensity_router_schema_candidate.json
- R224E_router_input_field_policy.md
- R224E_router_effect_computed_output_policy.md
- R224E_router_to_event_expansion_binding_summary.md
- R224E_teacher_default_visibility_policy.md
- R224E_review_ledger_trace_policy.md
- R224E_three_sample_regression_summary.md
- R224E_usage_boundary_and_not_publish_notice.md
- R224E_next_stage_handoff.md

## Review Questions

1. Are router input fields reused from R223P-5?
2. Is `router_effect` kept as computed output / ledger summary?
3. Are classroom event expansion affected fields listed?
4. Are teacher default visibility guards explicit?
5. Does review ledger preserve router trace?
6. Is three-sample regression summarized?
7. Is v0.2 still not published?
8. Are UI/R97B/runtime/prompt/model/db blocked?

## Decision Options

```text
A. PASS_LOCK_UNIT_ROUTER_STANDARD_CANDIDATE
B. HOLD_FOR_ROUTER_STANDARD_RECHECK
C. HOLD_FOR_R223P_V0_2_BINDING_RECHECK
```
