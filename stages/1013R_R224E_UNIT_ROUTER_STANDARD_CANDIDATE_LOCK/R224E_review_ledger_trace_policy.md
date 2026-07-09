# R224E Review Ledger Trace Policy

stage_id: 1013R_R224E_UNIT_ROUTER_STANDARD_CANDIDATE_LOCK

## Policy

Review ledger must preserve router trace.

## Required Ledger Trace

The ledger must record:

- router input values;
- router_effect summary;
- affected classroom_event_expansion fields;
- source_status;
- assumption_status;
- confidence or teacher confirmation need.

## Status Vocabulary

Use these statuses:

- source_evidence;
- system_inference;
- teacher_assumption;
- teacher_confirmation_required.

## Ledger Questions

The ledger must answer:

1. Why was this lesson routed this way?
2. Which source or assumption supports the route?
3. Which event fields were affected?
4. Which evidence should be collected?
5. What should the teacher confirm?

## Boundary

Review ledger is not teacher default manuscript. It must not execute components, call runtime/model, write lesson body, publish v0.2, or formal apply.
