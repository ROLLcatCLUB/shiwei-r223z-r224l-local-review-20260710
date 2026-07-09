# R224C Router Effect On Review Ledger Rules

stage_id: 1013R_R224C_ROUTER_TO_EVENT_EXPANSION_CONTRACT

## Rule

Review ledger must preserve router fields so reviewers can inspect why classroom event expansion became light, medium, or heavy.

## Required Ledger Fields

For every generated classroom event chain, review ledger must include:

- lesson_position_in_unit;
- unit_phase_role;
- practice_intensity;
- student_work_time_ratio;
- teacher_support_density;
- performance_task_link;
- stage_evidence_link;
- router_effect;
- source evidence / teacher assumption status.

## Required Explanations

The ledger must explain:

1. why the unit phase role was chosen;
2. why the practice intensity was chosen;
3. how student work time was inferred;
4. how teacher support density was inferred;
5. how performance task and stage evidence connect;
6. which classroom event fields changed because of the router.

## Source Status Rule

Ledger must distinguish:

- source_evidence;
- system_inference;
- teacher_assumption;
- teacher_confirmation_required.

## Ledger Guard

Review ledger may show raw router field names.

Teacher default manuscript must not.

Ledger must not trigger runtime, component execution, writeback, or formal apply.
