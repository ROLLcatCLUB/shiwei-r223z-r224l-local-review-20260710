# R224A Performance Task And Stage Evidence Link Rules

stage_id: 1013R_R224A_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING

## Purpose

The router must connect a lesson to the unit performance task and stage evidence.

Without this connection, a lesson may be expanded beautifully but still fail to serve the unit.

## performance_task_link

Required object:

```json
{
  "task_name": "...",
  "task_contribution": "...",
  "teacher_confirmation_required": true
}
```

Use it to answer:

- What final or staged performance task does this lesson support?
- Does this lesson produce, prepare, or evaluate part of that task?
- Does the teacher need to confirm the task direction before generation?

## stage_evidence_link

Required object:

```json
{
  "evidence_name": "...",
  "evidence_type": "observation_record | trial_sample | process_photo | draft | finished_work | oral_explanation | self_peer_evaluation",
  "collection_timing": "...",
  "assessment_use": "..."
}
```

Use it to answer:

- What evidence should be left by this lesson?
- When should the evidence be collected?
- How does it support later evaluation or unit performance task completion?

## Guard

Do not collect evidence for its own sake.

Evidence must correspond to:

- the current lesson responsibility;
- student action;
- teacher judgment;
- unit performance task or stage assessment.
