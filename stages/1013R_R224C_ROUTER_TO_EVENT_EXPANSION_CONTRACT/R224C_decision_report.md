# R224C Decision Report

stage_id: 1013R_R224C_ROUTER_TO_EVENT_EXPANSION_CONTRACT
status: PASS_LOCAL_PENDING_REVIEW

## Summary

R224C defines the transmission contract from `unit_lesson_practice_intensity_router` to `classroom_event_expansion`.

It answers:

```text
router output -> classroom event fields -> teacher manuscript rhythm -> review ledger -> screen / learning sheet / evidence rules
```

## Contract Coverage

R224C covers:

- event density rules for all six `unit_phase_role` values;
- router output to classroom event field mapping;
- teacher default manuscript naturalization rules;
- review ledger preservation rules;
- screen / learning sheet / evidence variation rules;
- three-sample contract trace;
- risk and misuse controls.

## Boundary

```text
No R97B.
No formal route.
No frontend/backend.
No runtime/provider/model.
No prompt.
No database.
No lesson body writeback.
No R223M/N/O teacher manuscript edits.
No R222D component library edits.
No v0.2 publication.
No HTML.
No formal apply.
```

## Decision Target

```text
PASS_CONTINUE_TO_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING
```

Alternative decisions:

```text
HOLD_FOR_ROUTER_TO_EVENT_MAPPING_REWORK
HOLD_FOR_UNIT_SOURCE_EVIDENCE_RECHECK
```
