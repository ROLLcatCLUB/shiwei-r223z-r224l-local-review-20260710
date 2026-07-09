# R224B Teacher Default View Impact Check

stage_id: 1013R_R224B_ROUTER_FIXTURE_AND_REGRESSION

## Policy

Router fields should shape teacher-facing manuscripts, but field names should not appear in the teacher default view.

Teacher default view should not display raw router field names.

## Hidden In Teacher Default View

The following field names are not teacher-facing labels:

- lesson_position_in_unit
- unit_phase_role
- practice_intensity
- student_work_time_ratio
- teacher_support_density
- router_effect
- performance_task_link
- stage_evidence_link

## Visible As Teaching Shape

The teacher should see the effect in natural manuscript form:

### 我为文具代言

Visible effect:

- longer student work block;
- teacher circulation language;
- process photo and design reason evidence;
- stronger showcase / explanation.

### 有趣的纸印

Visible effect:

- material observation;
- technique demonstration;
- trial sample;
- print-method comparison;
- learning sheet evidence.

### 色彩的碰撞

Visible effect:

- life color observation;
- red-yellow-blue starting point;
- color mixing micro-practice;
- color naming and visual expression;
- no heavy painting-product pressure.

## Regression Rule

Teacher default view should not say:

```text
unit_phase_role = ...
practice_intensity = ...
teacher_support_density = ...
```

It should express the result as a readable teaching manuscript.
