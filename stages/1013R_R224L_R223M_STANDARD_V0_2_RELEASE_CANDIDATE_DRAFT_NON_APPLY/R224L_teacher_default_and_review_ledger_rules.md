# R224L Teacher Default And Review Ledger Rules

## Teacher Default Rule

Teacher default manuscripts must use natural teaching language. They must not expose router field names or bridge metadata.

Blocked in teacher default:

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
performance_task_link
stage_evidence_link
router_effect
event_count_bias
checkpoint_density_hint
```

Allowed in teacher default:

```text
这节课先重观察，不急着做完整作品。
这节课要给学生更多实践时间，教师巡视时重点看过程证据。
两课递进时，要让第一课留下的试验记录进入第二课选择。
多课项目中，要把每一课的证据串成完整项目链。
```

## Review Ledger Rule

Review ledger may retain raw fields and computed bridge summaries for audit.

Allowed in review ledger:

```text
router_input_values
computed_router_effect_summary
affected_classroom_event_expansion_fields
teacher-facing naturalized implication
leak checks
publication status
```

## Separation Rule

```text
teacher default = clean / naturalized / teacher-readable
review ledger = trace retained / audit-readable
```

The release candidate draft does not modify any existing teacher manuscript.

