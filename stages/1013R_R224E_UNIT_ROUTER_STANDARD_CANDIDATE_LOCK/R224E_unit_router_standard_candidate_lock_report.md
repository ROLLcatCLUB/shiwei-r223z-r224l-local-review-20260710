# R224E Unit Router Standard Candidate Lock Report

stage_id: 1013R_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK
status: STANDARD_CANDIDATE_LOCK_ONLY

## Purpose

R224E locks `unit_lesson_practice_intensity_router` as a standard candidate.

It is a companion sub-standard candidate for the R223P-5 v0.2 candidate. It is not a formal standard release and does not publish `R223M_STANDARD_V0_2`.

## Input Lineage

```text
R224A = PASS_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING
R224B = PASS_ROUTER_FIXTURE_AND_REGRESSION
R224C = PASS_ROUTER_TO_EVENT_EXPANSION_CONTRACT
R224D = PASS_ROUTER_CONTRACT_SCHEMA_BINDING
```

## Locked Findings

1. Router input fields reuse R223P-5 v0.2 candidate fields.
2. R224E does not create duplicate router fields.
3. `router_effect` is not a required schema object.
4. `router_effect` is a computed contract output and review ledger summary.
5. Router output can map into classroom event expansion fields.
6. Teacher default manuscript must naturalize router effects and hide raw field names.
7. Review ledger must preserve router trace, source status, assumptions, confidence, and affected event fields.
8. Three sample regression remains valid.

## Locked Status

```text
R224E = UNIT_ROUTER_STANDARD_CANDIDATE_LOCK
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI / R97B / runtime / prompt / model / db = BLOCKED
```

## Decision Target

```text
PASS_LOCK_UNIT_ROUTER_STANDARD_CANDIDATE
```
