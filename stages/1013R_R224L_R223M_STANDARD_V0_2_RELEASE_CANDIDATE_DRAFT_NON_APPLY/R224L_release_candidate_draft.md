# R224L R223M Standard v0.2 Release Candidate Draft

## Status

```text
R223M_STANDARD_V0_2_RELEASE_CANDIDATE_DRAFT = CREATED
R223M_STANDARD_V0_2 = NOT_PUBLISHED
formal_apply_allowed = false
```

This document is a release-candidate draft only. It is not a published standard and does not authorize runtime implementation, prompt changes, UI changes, database changes, teacher manuscript rewrites, or formal apply.

## Standard Candidate Name

```text
unit_lesson_practice_intensity_router
```

## Purpose

The router decides how a lesson should be expanded based on its position and responsibility inside a unit. It prevents every art lesson from being expanded into the same generic sequence.

It answers:

```text
What role does this lesson play in the unit?
How much student practice should it contain?
How much teacher support is needed?
How strongly should it connect to the unit performance task?
What stage evidence should remain?
How should classroom event expansion density change?
```

## Locked Router Input Fields

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
performance_task_link
stage_evidence_link
```

No additional router input field is added in this candidate draft.

## Field Meanings

### unit_phase_role

Indicates the lesson's responsibility in the unit, such as introduction, technique preparation, practice creation, showcase evaluation, transfer closure, or project synthesis.

### lesson_position_in_unit

Indicates whether the lesson is early, middle, late, or final in the unit.

### practice_intensity

Indicates whether student practice should be low, medium, or high.

### student_work_time_ratio

Indicates how much class time should be given to student doing, making, testing, creating, rehearsing, presenting, or refining.

### teacher_support_density

Indicates how much teacher scaffolding, demonstration, rescue, checkpointing, and feedback is needed.

### performance_task_link

Indicates how this lesson connects to the unit-level performance task.

### stage_evidence_link

Indicates what evidence this lesson should leave for the unit evidence chain.

## Router Effect Bridge

`router_effect` is not a required schema object. It is a computed bridge from router inputs to classroom event expansion density.

Allowed bridge fields:

```text
event_count_bias
observation_time_bias
demonstration_time_bias
micro_practice_count_bias
formal_creation_time_bias
teacher_support_density_hint
checkpoint_density_hint
exit_condition_hint
```

## Classroom Event Expansion Influence

The router may influence:

```text
event count
observation time
demonstration time
micro-practice count
formal creation time
teacher support density
checkpoint density
exit condition
evidence collection timing
```

It must not automatically rewrite a teacher manuscript.

## Teacher Default Visibility Rule

Teacher default manuscripts must not expose raw router fields. The teacher-facing layer should translate router decisions into natural teaching language.

Example:

```text
Raw: practice_intensity = high
Teacher-facing: 这节课要把时间更多还给学生的实践推进，教师巡视时重点看过程证据和调整理由。
```

## Review Ledger Trace Rule

Review ledger may retain raw router input values, computed bridge summary, affected classroom event expansion fields, leak checks, and publication status.

The review ledger is for audit, not for default teacher reading.

## Publication Hold

This release-candidate draft is allowed because R224K passed publication readiness gate. Publication is still held.

```text
publication = HOLD_UNTIL_EXPLICIT_AUTHORIZATION
direct_publish_allowed = false
```

