# R224F Review Ledger Trace Check

stage_id: 1013R_R224F_ROUTER_STANDARD_EXTRA_UNIT_REGRESSION

## Policy

Review ledger must preserve router trace for every added sample.

## Required Ledger Fields

- router input values;
- router_effect summary;
- affected classroom_event_expansion fields;
- source_status;
- assumption_status;
- confidence / teacher confirmation need.

## Sample Trace Summary

| Sample | source_status | assumption_status | confidence | teacher confirmation |
| --- | --- | --- | --- | --- |
| 红红的剪纸 | system_inference | teacher_confirmation_required | medium | confirm unit position and actual technique sequence |
| 寓言与神话 | system_inference | teacher_confirmation_required | medium | confirm project product and story source |
| 美术大家庭 | system_inference | teacher_confirmation_required | medium | confirm unit role and local life examples |

## Affected Event Fields Checked

Each sample records:

- event_count_bias;
- explanation_density;
- demonstration_density;
- micro_practice_count;
- formal_creation_time;
- teacher_circulation_focus;
- showcase_evaluation_intensity;
- learning_sheet_fields;
- evidence_collection_mode;
- checkpoint;
- exit_condition.

## Result

```text
review_ledger_trace = pass
```
