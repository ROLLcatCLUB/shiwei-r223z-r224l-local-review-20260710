# R224B Sample M Router Expansion Fixture

sample_id: M_stationery
sample_name: 我为文具代言
fixture_type: router_expansion_regression

## Router Profile

```json
{
  "sample_id": "M_stationery",
  "lesson_position_in_unit": "late",
  "unit_phase_role": "practice_creation",
  "practice_intensity": "high",
  "student_work_time_ratio": "high",
  "teacher_support_density": "heavy",
  "performance_task_link": {
    "task_name": "一年级购买文具建议书 / 文具课堂使用指南 / 文具代言展示",
    "task_contribution": "改造文具的草图、过程照片、作品展示和设计理由，为最终建议书、使用指南和代言展示提供证据。",
    "teacher_confirmation_required": true
  },
  "stage_evidence_link": {
    "evidence_name": "改造草图、过程照片、作品展示说明",
    "evidence_type": ["draft", "process_photo", "finished_work", "oral_explanation"],
    "collection_timing": ["1+1 合作小设计", "1+n 文具大变身", "笔友汇展示"],
    "assessment_use": "判断学生是否能发现使用问题、选择材料解决问题并表达设计理由。"
  },
  "router_effect": {
    "explanation_density": "medium",
    "demonstration_density": "targeted",
    "micro_practice_count": "1-2",
    "formal_creation_time": "high",
    "teacher_circulation_focus": ["材料选择理由", "功能是否服务使用问题", "合作分工", "制作卡点", "过程证据"],
    "showcase_evaluation_intensity": "high",
    "learning_sheet_fields": ["使用问题", "材料选择", "改造理由", "同伴建议"],
    "evidence_collection_mode": ["process_photo", "draft", "finished_work", "oral_explanation"]
  }
}
```

## Expected Classroom Expansion Effect

This sample should not be written as a long teacher explanation lesson. It should protect student making time.

Expected shifts:

- whole-class explanation is used to set design purpose, not to dominate the period;
- demonstration is targeted at bottlenecks such as attaching, wrapping, combining, or stabilizing materials;
- micro-practice is short and used only when students cannot transfer a sketch into a simple object;
- student creation time is the main time block;
- teacher circulation focuses on whether the improvement serves a real use problem;
- process photos, design reasons, and oral explanation carry heavier evidence weight;
- showcase and evaluation are stronger because the lesson is near the unit performance task.

## Regression Pass Signal

The fixture passes if the expansion clearly reads as a late-unit practice creation lesson with heavy support, not as an introduction or technique-preparation lesson.
