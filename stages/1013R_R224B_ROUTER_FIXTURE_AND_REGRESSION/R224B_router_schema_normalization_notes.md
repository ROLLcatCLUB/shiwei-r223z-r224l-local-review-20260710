# R224B Router Schema Normalization Notes

stage_id: 1013R_R224B_ROUTER_FIXTURE_AND_REGRESSION

## Why Normalization Is Needed

R224A defined a planning schema. Its `router_effect.density_values` listed:

```json
["low", "medium", "high"]
```

But real fixture values need more than density enums. R224B clarifies field types so later validators do not over-normalize rich classroom routing information.

## Normalized Field Types

| Field | Type | Allowed / expected values |
| --- | --- | --- |
| explanation_density | density_enum | low / medium / high |
| demonstration_density | density_or_strategy | low / medium / high / targeted / rescue / comparison |
| micro_practice_count | count_range | 0-1 / 1-2 / 1-3 / 2-3 |
| formal_creation_time | density_enum | low / medium / high |
| teacher_circulation_focus | text_or_list | natural language or list |
| showcase_evaluation_intensity | density_enum | low / medium / high |
| learning_sheet_fields | list | field names visible to review ledger, not necessarily teacher default view |
| evidence_collection_mode | text_or_list | evidence modes and timing |

## Regression Guard

Do not force every `router_effect` value into low / medium / high.

The router needs:

- density enums for broad intensity;
- ranges for count-like decisions;
- strategy labels for demonstration style;
- natural language / list fields for teacher observation and evidence details.

## Teacher Default View Rule

Teacher default manuscript should not display these router field names:

- lesson_position_in_unit;
- unit_phase_role;
- practice_intensity;
- student_work_time_ratio;
- teacher_support_density;
- router_effect.

These fields belong in review ledger or backend planning records.
