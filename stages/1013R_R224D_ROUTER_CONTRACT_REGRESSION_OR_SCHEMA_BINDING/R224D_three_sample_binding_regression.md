# R224D Three Sample Binding Regression

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING

## Regression Purpose

Confirm that R224C contract fields can bind to R223P-5 candidate schema and still preserve the three sample routing decisions.

## M. 我为文具代言

Router:

```text
late / practice_creation / high / high / heavy
```

Binding:

- unit_phase_role -> existing R223P-5 field;
- lesson_position_in_unit -> existing R223P-5 field;
- practice_intensity -> existing R223P-5 field;
- student_work_time_ratio -> existing R223P-5 field;
- teacher_support_density -> existing R223P-5 field;
- performance_task_link -> existing R223P-5 field;
- stage_evidence_link -> existing R223P-5 field;
- checkpoint -> existing R223P-5 field;
- event_count_bias and creation-time effects -> computed contract output, ledger trace.

Pass signal:

The binding supports a creation-serving event chain without adding new required schema fields.

## N. 有趣的纸印

Router:

```text
middle / technique_preparation / medium / medium / normal
```

Binding:

- technique_preparation maps to existing unit_phase_role;
- demonstration and micro-practice details map to demonstration_type / micro_practice_type where needed;
- learning_sheet_fields stays ledger-only;
- evidence_collection_mode maps to evidence_trigger.details, process_evidence, or stage_evidence_link.

Pass signal:

The binding supports trial sample and method comparison without converting the lesson into final product pressure.

## O. 色彩的碰撞

Router:

```text
early / intro_understanding / medium / medium / normal
```

Binding:

- intro_understanding maps to existing unit_phase_role;
- color observation and visual expression can use aesthetic_language_focus if needed;
- micro-practice count remains derived planning metadata;
- evidence mode maps to observation record, color trial, naming note, and oral explanation evidence.

Pass signal:

The binding supports an early visual understanding lesson without creating a heavy creation lesson or science-only experiment.

## Overall Result

```text
three_sample_binding_regression = PASS
```
