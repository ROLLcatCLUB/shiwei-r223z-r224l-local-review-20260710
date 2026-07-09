# R224A Three Sample Router Fixture

stage_id: 1013R_R224A_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING
fixture_status: planning_fixture_only

## Fixture A. 我为文具代言

```json
{
  "sample_id": "M_stationery",
  "lesson_title": "我为文具代言：智造·新朋友",
  "unit_title": "我为文具代言",
  "lesson_position_in_unit": "late",
  "unit_phase_role": "practice_creation",
  "practice_intensity": "high",
  "student_work_time_ratio": "high",
  "teacher_support_density": "heavy",
  "performance_task_link": {
    "task_name": "一年级购买文具建议书 / 文具课堂使用指南 / 文具代言展示",
    "task_contribution": "通过文具改造和展示表达，为最终建议书、使用指南和代言展示提供设计理由与作品证据。",
    "teacher_confirmation_required": true
  },
  "stage_evidence_link": {
    "evidence_name": "改造草图、过程照片、作品展示说明",
    "evidence_type": "draft | process_photo | finished_work | oral_explanation",
    "collection_timing": "1+1 合作小设计、1+n 文具大变身、笔友汇展示",
    "assessment_use": "判断学生是否能发现使用问题、选择材料解决问题并表达设计理由。"
  },
  "router_effect": {
    "explanation_density": "medium",
    "demonstration_density": "targeted",
    "micro_practice_count": "1-2",
    "formal_creation_time": "high",
    "teacher_circulation_focus": "材料选择理由、功能是否服务使用问题、合作分工、制作卡点、展示表达",
    "showcase_evaluation_intensity": "high",
    "learning_sheet_fields": [
      "我想解决的文具使用问题",
      "我选择的材料",
      "我的改造理由",
      "同伴建议"
    ],
    "evidence_collection_mode": "process photo + draft + finished work + oral explanation"
  }
}
```

## Fixture B. 有趣的纸印

```json
{
  "sample_id": "N_paper_print",
  "lesson_title": "有趣的纸印",
  "unit_title": "纸印探究 / 纸材与印痕",
  "lesson_position_in_unit": "middle",
  "unit_phase_role": "technique_preparation",
  "practice_intensity": "medium",
  "student_work_time_ratio": "medium",
  "teacher_support_density": "normal",
  "performance_task_link": {
    "task_name": "纸印作品与印痕说明",
    "task_contribution": "通过纸材观察、试印记录和印法比较，为后续纸印作品完成提供技法依据。",
    "teacher_confirmation_required": true
  },
  "stage_evidence_link": {
    "evidence_name": "纸材预测记录、试印小样、印法比较记录、保底作品",
    "evidence_type": "observation_record | trial_sample | finished_work | oral_explanation",
    "collection_timing": "纸材观察、第一次转印、干湿油印比较、作品说明",
    "assessment_use": "判断学生是否能把纸材、印法和印痕效果建立联系。"
  },
  "router_effect": {
    "explanation_density": "medium",
    "demonstration_density": "medium",
    "micro_practice_count": "2-3",
    "formal_creation_time": "medium",
    "teacher_circulation_focus": "纸材肌理观察、上色多少、按压方式、揭纸动作、试印记录",
    "showcase_evaluation_intensity": "medium",
    "learning_sheet_fields": [
      "纸材预测",
      "试印结果",
      "印法比较",
      "我发现的印痕特点"
    ],
    "evidence_collection_mode": "trial sample + learning sheet + small work"
  }
}
```

## Fixture C. 色彩的碰撞

```json
{
  "sample_id": "O_color_collision",
  "lesson_title": "色彩的碰撞",
  "unit_title": "色彩观察与表达",
  "lesson_position_in_unit": "early",
  "unit_phase_role": "intro_understanding",
  "practice_intensity": "medium",
  "student_work_time_ratio": "medium",
  "teacher_support_density": "normal",
  "performance_task_link": {
    "task_name": "色彩创想会 / 色彩表达小作品",
    "task_contribution": "通过校园色彩观察、红黄蓝调色微练和色彩差异表达，为后续色彩表达任务建立经验。",
    "teacher_confirmation_required": true
  },
  "stage_evidence_link": {
    "evidence_name": "生活色彩观察记录、调色微练、色彩命名与表达",
    "evidence_type": "observation_record | trial_sample | oral_explanation",
    "collection_timing": "校园取色、两色相碰、同色差异比较、色彩创想会",
    "assessment_use": "判断学生是否能观察生活色彩、发现调色差异并用视觉语言表达感受。"
  },
  "router_effect": {
    "explanation_density": "medium",
    "demonstration_density": "medium",
    "micro_practice_count": "2",
    "formal_creation_time": "medium",
    "teacher_circulation_focus": "调色比例、冷暖偏向、明暗差异、色彩命名和画面感受",
    "showcase_evaluation_intensity": "medium",
    "learning_sheet_fields": [
      "我在生活中看到的颜色",
      "我调出的新颜色",
      "它更偏向什么颜色",
      "它让我想到什么"
    ],
    "evidence_collection_mode": "color trial + naming note + brief expression"
  }
}
```

## Fixture Guard

The three samples intentionally route differently:

- stationery: late / practice_creation / high practice;
- paper print: middle / technique_preparation / medium practice;
- color collision: early / intro_understanding / medium practice.

This prevents the classroom event expansion layer from treating all art lessons as the same creation-heavy lesson.
