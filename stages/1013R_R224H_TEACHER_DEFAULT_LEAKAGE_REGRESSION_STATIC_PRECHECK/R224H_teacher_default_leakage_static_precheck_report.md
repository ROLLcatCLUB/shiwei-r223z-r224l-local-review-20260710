# R224H Teacher Default Leakage Static Precheck Report

stage_id: 1013R_R224H_TEACHER_DEFAULT_LEAKAGE_REGRESSION_STATIC_PRECHECK
status: STATIC_PRECHECK_ONLY

## Purpose

R224H performs a static leakage precheck for the unit lesson practice intensity router candidate.

It checks whether raw router fields or `router_effect` fields appear in teacher-facing naturalized text samples.

This is not runtime generation. It does not call provider/model, does not change prompt, does not create formal teacher manuscripts, does not write database, does not publish v0.2, and does not touch UI/R97B.

## Source

```text
R224E = PASS_LOCK_UNIT_ROUTER_STANDARD_CANDIDATE
R224F = PASS_EXTRA_UNIT_REGRESSION
R224G = PASS_SUMMARY_READY_AND_HOLD_PUBLICATION
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

## Samples

| Sample | Unit structure | Check target |
| --- | --- | --- |
| 红红的剪纸 | technique_preparation_unit | Teacher text should mention safe trial, fold-cut method, and pattern comparison without raw router fields |
| 寓言与神话 | project_synthesis_unit | Teacher text should mention project synthesis, evidence assembly, and story expression without raw router fields |
| 美术大家庭 | appreciation_intro_understanding_unit | Teacher text should mention observation, classification, and life connection without raw router fields |

## Forbidden Raw Fields

Teacher-facing text must not include:

- unit_phase_role
- lesson_position_in_unit
- practice_intensity
- student_work_time_ratio
- teacher_support_density
- performance_task_link
- stage_evidence_link
- router_effect
- event_count_bias
- micro_practice_count
- checkpoint
- exit_condition
- formal_creation_time

## Result

```text
R224H = PASS_STATIC_LEAKAGE_PRECHECK
forbidden_token_leak_count = 0
review_ledger_trace_retained = true
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

## Boundary

```text
No HTML.
No R97B.
No frontend/backend.
No runtime/provider/model.
No prompt change.
No database.
No lesson body writeback.
No R222D component library modification.
No M/N/O teacher manuscript modification.
No formal apply.
No v0.2 publication.
```
