# R224E Router Effect Computed Output Policy

stage_id: 1013R_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK

## Locked Decision

`router_effect` is not a required schema object.

It is locked as:

```text
computed contract output
review ledger summary
bridge into classroom_event_expansion fields
```

## Why

`router_effect` includes mixed information:

- event count bias;
- explanation density;
- demonstration density or strategy;
- micro-practice count range;
- formal creation time;
- teacher circulation focus;
- showcase/evaluation intensity;
- learning sheet fields;
- evidence collection mode;
- checkpoint;
- exit condition.

These should not be forced into one required formal schema object.

## Locked Mapping

| router_effect item | Locked policy |
| --- | --- |
| event_count_bias | computed planning output / ledger summary |
| explanation_density | optional event planning metadata |
| demonstration_density | maps to demonstration_type plus density/strategy note |
| micro_practice_count | optional count range, maps to micro_practice_type when needed |
| formal_creation_time | optional planning metadata |
| teacher_circulation_focus | checkpoint / support note / ledger trace |
| showcase_evaluation_intensity | optional planning metadata |
| learning_sheet_fields | existing review-ledger-only field |
| evidence_collection_mode | maps to evidence_trigger.details / process_evidence / stage_evidence_link |
| checkpoint | existing R223P-5 candidate field |
| exit_condition | existing R223P-5 candidate field |

## Guard

Future stages must not promote `router_effect` to formal required schema without additional regression and explicit approval.
