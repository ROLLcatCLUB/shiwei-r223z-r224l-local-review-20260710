# R224D Teacher Default Visibility Guard

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING

## Rule

Teacher default manuscript must not display router field names or schema field labels.

## Hidden Field Names

The following must not appear as visible labels in teacher default manuscripts:

- unit_phase_role;
- lesson_position_in_unit;
- practice_intensity;
- student_work_time_ratio;
- teacher_support_density;
- performance_task_link;
- stage_evidence_link;
- router_effect;
- event_count_bias;
- explanation_density;
- demonstration_density;
- micro_practice_count;
- formal_creation_time;
- teacher_circulation_focus;
- showcase_evaluation_intensity;
- evidence_collection_mode;
- checkpoint;
- exit_condition.

## Naturalized Effects

The teacher default manuscript may show:

- a short unit position paragraph;
- more or less teacher explanation;
- more or less student work time;
- demonstration and trial rhythm;
- teacher circulation reminders;
- evidence and transition language;
- evaluation or showcase emphasis.

## Binding With R223P-5

R223P-5 already marks these fields as naturalized, hidden, or ledger-only. R224D keeps that rule.

## Guard

If a future generated teacher manuscript contains raw router/schema labels, it must be treated as a manuscript rendering defect, not a schema feature.
