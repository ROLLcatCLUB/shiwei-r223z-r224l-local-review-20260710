# R224A Report

stage_id: 1013R_R224A_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING
status: PASS_LOCAL_PENDING_REVIEW

## Summary

R224A creates the planning contract for `unit_lesson_practice_intensity_router`.

It pulls the R223 classroom event expansion standard back to the unit level by asking:

```text
What role does this lesson play in the unit, and how much classroom practice/support/evidence should it generate?
```

## Completed Outputs

- router contract;
- schema v0.1;
- phase role registry;
- practice intensity decision rules;
- student work time ratio rules;
- teacher support density rules;
- performance task and stage evidence link rules;
- router effect on classroom event expansion;
- three-sample router fixture;
- risk and misuse notes.

## Three Sample Decisions

| Sample | lesson_position_in_unit | unit_phase_role | practice_intensity | student_work_time_ratio | teacher_support_density |
| --- | --- | --- | --- | --- | --- |
| 我为文具代言 | late | practice_creation | high | high | heavy |
| 有趣的纸印 | middle | technique_preparation | medium | medium | normal |
| 色彩的碰撞 | early | intro_understanding | medium | medium | normal |

## Boundary

```text
No R97B changes.
No route changes.
No frontend/backend changes.
No runtime/provider/model/prompt/db.
No lesson body writeback.
No R223M/N/O teacher manuscript edits.
No R222D component library edits.
No v0.2 publication.
No HTML page.
No formal apply.
```

## Decision Target

```text
PASS_CONTINUE_TO_R224B_ROUTER_FIXTURE_AND_REGRESSION
```

If review finds router schema problems, use:

```text
HOLD_FOR_ROUTER_SCHEMA_REWORK
```

If review finds source evidence uncertainty, use:

```text
HOLD_FOR_UNIT_SOURCE_EVIDENCE_RECHECK
```
