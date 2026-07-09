# R224F Teacher Visibility Leak Check

stage_id: 1013R_R224F_ROUTER_STANDARD_EXTRA_UNIT_REGRESSION

## Policy

Teacher default manuscripts must not show raw router field names or `router_effect` field names.

## Forbidden In Teacher Default View

- unit_phase_role
- lesson_position_in_unit
- practice_intensity
- student_work_time_ratio
- teacher_support_density
- performance_task_link
- stage_evidence_link
- router_effect
- event_count_bias
- explanation_density
- demonstration_density
- micro_practice_count
- formal_creation_time
- teacher_circulation_focus
- showcase_evaluation_intensity
- learning_sheet_fields
- evidence_collection_mode
- checkpoint
- exit_condition

## Regression Check By Sample

### 红红的剪纸

Natural teacher-facing effect:

- first demonstrate and try a safe fold-cut method;
- keep the work modest enough for technique preparation;
- observe safety, fold direction, connected patterns, and unfolding result.

No raw router field should appear.

### 寓言与神话

Natural teacher-facing effect:

- protect project-making time;
- help students connect character, plot, scene, material, and meaning;
- collect drafts, process evidence, and presentation explanation.

No raw router field should appear.

### 美术大家庭

Natural teacher-facing effect:

- focus on finding art in life;
- classify and explain examples;
- avoid heavy creation pressure.

No raw router field should appear.

## Result

```text
teacher_visibility_leak = false
```
