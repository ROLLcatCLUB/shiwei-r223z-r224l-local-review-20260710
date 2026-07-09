# R224E Teacher Default Visibility Policy

stage_id: 1013R_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK

## Policy

Teacher default manuscript must not display raw router or router_effect field names.

## Forbidden Raw Field Names

The following names are forbidden in teacher default manuscript as labels:

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
- learning_sheet_fields;
- evidence_collection_mode;
- checkpoint;
- exit_condition.

## Allowed Naturalized Expressions

Teacher manuscript may show:

- this lesson first helps students observe and name the problem;
- students need a short trial before the later work;
- the main time should be protected for making and revising;
- the teacher should circulate to watch material choice, method use, and evidence;
- the lesson closes by selecting evidence for the unit performance task.

## Rendering Rule

If raw field labels leak into teacher default manuscript, treat it as rendering failure, not a schema feature.
