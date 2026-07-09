# R224D Router Contract Schema Binding Check

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING
status: SCHEMA_BINDING_CHECK_ONLY

## Purpose

R224D checks whether the R224C `router -> classroom_event_expansion` contract can bind to the R223P-5 v0.2 candidate schema without field conflict, duplication, or premature publication.

R224D does not publish v0.2, does not modify R223M/N/O teacher manuscripts, does not create HTML, and does not start UI/R97B/runtime/model/prompt/db work.

## Source Artifacts

- R223P-5: `R223P_5_classroom_event_schema_v0_2_candidate.json`
- R223P-5: `R223P_5_unit_lesson_practice_intensity_router_contract.md`
- R223P-5: `R223P_5_field_required_optional_ledger_only_policy.md`
- R224C: `R224C_router_output_to_event_field_mapping.json`

## Binding Summary

R224C is compatible with R223P-5 when interpreted as follows:

1. Core router inputs are already covered by R223P-5 candidate fields.
2. `checkpoint` and `exit_condition` are already covered as general pedagogy candidate fields.
3. `learning_sheet_fields` is already review-ledger-only in R223P-5.
4. `router_effect` should not become one monolithic formal schema object.
5. Most `router_effect` values should be treated as derived event expansion controls.
6. Some derived fields may enter review ledger or optional event metadata later, but not as teacher-visible fields.

## Compatibility Decision

```text
R224C router contract = compatible_with_R223P_5_v0_2_candidate
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

## Binding Guard

Do not duplicate R223P-5 fields under new R224D names.

Do not expose router fields in teacher default manuscripts.

Do not force rich effect fields into only low/medium/high values.
