# README FOR GPT REVIEW

stage_id: 1013R_R224A_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING
package_type: planning_contract_review

## Review Purpose

R224A establishes a planning contract for the unit-level lesson practice intensity router.

It does not start UI, R97B, runtime, model, prompt, database, or formal apply. It does not edit existing R223M/N/O teacher manuscripts.

## Review Focus

Check whether the router answers:

1. where the lesson sits in the unit;
2. what phase responsibility it carries;
3. how practice-heavy it should be;
4. how much student work time it needs;
5. how much teacher support it needs;
6. how it links to the unit performance task;
7. what stage evidence it should leave;
8. how those answers change classroom event expansion density.

## Key Files

- R224A_unit_lesson_practice_intensity_router_contract.md
- R224A_router_schema_v0_1.json
- R224A_unit_phase_role_registry.md
- R224A_practice_intensity_decision_rules.md
- R224A_student_work_time_ratio_rules.md
- R224A_teacher_support_density_rules.md
- R224A_performance_task_and_stage_evidence_link_rules.md
- R224A_router_effect_on_classroom_event_expansion.md
- R224A_three_sample_router_fixture.md
- R224A_risk_and_misuse_notes.md
- R224A_report.md

## Decision Options

```text
A. PASS_CONTINUE_TO_R224B_ROUTER_FIXTURE_AND_REGRESSION
B. HOLD_FOR_ROUTER_SCHEMA_REWORK
C. HOLD_FOR_UNIT_SOURCE_EVIDENCE_RECHECK
```

## Boundary

No R97B, no route, no frontend/backend, no runtime/provider/model, no prompt, no database, no lesson body writeback, no R223M/N/O edits, no R222D edits, no v0.2 publication, no HTML, no formal apply.
