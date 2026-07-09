# R224D Review Ledger Router Trace Policy

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING

## Rule

Review ledger can and should preserve router fields.

## Required Router Trace

For each lesson-level classroom event chain, review ledger should record:

- unit_phase_role;
- lesson_position_in_unit;
- practice_intensity;
- student_work_time_ratio;
- teacher_support_density;
- performance_task_link;
- stage_evidence_link;
- router_effect as computed summary;
- source_status;
- assumption_status;
- confidence or confirmation need.

## Source / Assumption Status

Use these status categories:

- source_evidence: directly supported by sample or unit design;
- system_inference: inferred from lesson position, task type, or classroom pattern;
- teacher_assumption: plausible but teacher should confirm;
- teacher_confirmation_required: cannot be treated as final until teacher confirms.

## Trace Format

The ledger should answer:

```text
Why was this lesson routed this way?
Which source or assumption supports it?
Which classroom event fields changed because of the router?
What teacher confirmation remains?
```

## Not Allowed

The ledger must not:

- become teacher default manuscript;
- execute components;
- trigger runtime/model;
- write lesson body;
- publish v0.2;
- formal apply.
