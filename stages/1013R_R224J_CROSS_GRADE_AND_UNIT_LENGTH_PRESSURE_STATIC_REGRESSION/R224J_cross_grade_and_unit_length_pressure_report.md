# R224J Cross Grade And Unit Length Pressure Static Regression Report

## Result

```text
R224J = PASS_CROSS_GRADE_AND_LENGTH_STATIC_REGRESSION
R223M_STANDARD_V0_2 = NOT_PUBLISHED
router_effect_required_schema_object = false
teacher_default_field_leak = false
required_schema_object_leak = false
```

## Purpose

R224J checks whether the `unit_lesson_practice_intensity_router` candidate can survive two forms of pressure:

1. Different grade bands: low, middle, high.
2. Different unit length types: single-lesson short task, two-lesson progression, multi-lesson project.

This is a static regression only. It does not generate real teacher manuscripts, does not touch R223M/N/O source-of-truth manuscripts, and does not publish v0.2.

## Main Finding

The existing router input field set is sufficient for this pressure test. No new router input field is required.

The field set remains:

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
performance_task_link
stage_evidence_link
```

`router_effect` remains a computed bridge and review-ledger summary. It does not become a required schema object.

## Cross-Grade Static Regression

| Grade Band | Example Type | Router Behavior |
|---|---|---|
| low | observation / game / simple material experience | More observation and game-like entry, less formal creation, light evidence. |
| middle | technique preparation / small project creation | Balanced observation, demonstration, micro-practice, and bounded creation. |
| high | design application / integrated expression | More synthesis, design reasoning, checkpoints, and student work time. |

## Unit-Length Static Regression

| Unit Length Type | Router Behavior |
|---|---|
| single_lesson_short_task | Keep event count bounded, shorten evidence chain, avoid over-building project logic. |
| two_lesson_progression | Split preparation and application, preserve clear stage evidence from each lesson. |
| multi_lesson_project | Increase checkpoint density, stage evidence linkage, and performance-task continuity. |

## Risk Check

The router does not flatten every lesson into the same sequence of:

```text
observe → demonstrate → micro-practice → create → evaluate
```

Instead, it changes density and emphasis according to grade band, unit role, lesson position, practice intensity, work-time ratio, teacher support density, performance task link, and stage evidence link.

## Decision

R224J passes as a static regression package. It still does not authorize v0.2 publication, formal UI, runtime, prompt changes, database writes, R97B, or formal apply.

