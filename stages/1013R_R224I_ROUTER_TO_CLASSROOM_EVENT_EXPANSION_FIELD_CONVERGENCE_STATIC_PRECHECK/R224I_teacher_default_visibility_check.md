# R224I Teacher Default Visibility Check

## Result

```text
teacher_default_field_leak = false
```

## Visibility Rule

Teacher default manuscripts should not show raw router fields such as:

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

Instead, teacher-facing language should be naturalized.

## Naturalized Examples

| Sample | Teacher-Facing Implication |
|---|---|
| 红红的剪纸 | 先用小样看懂折与剪的关系，多做慢示范和即时巡视。 |
| 寓言与神话 | 把一个关键故事瞬间画清楚，巡视重点看画面主次、人物动作和故事意思。 |
| 美术大家庭 | 从生活里发现美术，用关系图说清门类与生活变化，不安排重创作。 |

## Conclusion

The router may inform manuscript generation, but raw field names remain hidden from the teacher default reading layer.

