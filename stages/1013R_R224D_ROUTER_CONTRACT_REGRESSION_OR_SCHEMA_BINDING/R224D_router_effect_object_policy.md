# R224D Router Effect Object Policy

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING

## Decision

`router_effect` should not become a single required object in the formal v0.2 candidate schema at this stage.

router_effect should not become a single required object.

## Reason

`router_effect` is a derived planning result. It includes mixed field types:

- density enum;
- density or strategy label;
- count range;
- text/list;
- computed screen/sheet/evidence expectations.

Promoting it as one formal required object would duplicate or blur existing R223P-5 fields such as:

- practice_intensity;
- student_work_time_ratio;
- teacher_support_density;
- checkpoint;
- exit_condition;
- process_evidence;
- learning_sheet_fields;
- evidence_trigger.details;
- demonstration_type;
- micro_practice_type.

## Binding Policy

Use `router_effect` as a computed bridge:

```text
router input fields
-> derived event expansion controls
-> teacher manuscript rhythm
-> review ledger trace
```

## Field-Level Recommendations

| Derived field | Recommendation |
| --- | --- |
| event_count_bias | computed planning output, ledger visible |
| explanation_density | optional event planning metadata |
| demonstration_density | map to demonstration_type plus density note |
| micro_practice_count | optional derived count, do not replace micro_practice_type |
| formal_creation_time | optional event planning metadata |
| teacher_circulation_focus | map to checkpoint / teacher scaffolding / ledger note |
| showcase_evaluation_intensity | optional planning metadata for showcase_evaluation |
| learning_sheet_fields | existing ledger-only field |
| evidence_collection_mode | map to evidence_trigger.details / process_evidence / stage_evidence_link |
| checkpoint | existing candidate field |
| exit_condition | existing candidate field |

## Teacher Default Guard

`router_effect` and its raw field names must not appear in teacher default manuscripts.
