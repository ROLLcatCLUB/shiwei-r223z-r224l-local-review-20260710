# R224J Teacher Default Visibility Check

## Result

```text
teacher_default_field_leak = false
```

## Rule

Teacher default text must not expose raw router fields:

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

## Static Regression Result

The matrices only use teacher-facing naturalized implications in the default-facing layer. The raw fields stay in the review matrices and ledger trace.

Examples:

| Pressure Type | Naturalized Teacher Implication |
|---|---|
| Low grade | 先把眼睛和语言打开，不急着做完整作品。 |
| Middle grade | 把示范和小练分开，巡视时看方法是否真正用起来。 |
| High grade | 把时间还给方案推进和证据表达。 |
| Single lesson | 控制任务，不把观察课扩成完整创作课。 |
| Two lessons | 让第一课证据进入第二课。 |
| Multi-lesson | 把每一课留下的证据串成项目链。 |

## Conclusion

R224J keeps router logic out of teacher-visible field labels while preserving its influence on classroom event density.

