# R224A Unit-Lesson Practice Intensity Router Contract

stage_id: 1013R_R224A_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING
status: PLANNING_CONTRACT_ONLY

## Purpose

R224A establishes a planning contract for `unit_lesson_practice_intensity_router`.

The router answers one core question:

```text
How much should this lesson expand into classroom practice, support, demonstration, evidence collection, and teacher guidance, given its position and responsibility inside the unit?
```

R224A does not generate a new formal lesson manuscript. It does not modify R223M/N/O teacher manuscripts. It does not publish v0.2. It does not start UI, R97B, runtime, provider/model, prompt, database, or formal apply work.

## Why This Router Is Needed

R223 proved that classroom event expansion can produce teacher-readable manuscripts. But not every lesson in a unit should be expanded with the same density.

Some lessons mainly help students understand concepts or observe examples. Some prepare techniques. Some are practice-heavy creation lessons. Some are showcase and evaluation lessons. A system that expands every lesson as `observe -> demonstrate -> micro-practice -> create -> evaluate` will overfit one classroom rhythm and overload simple or appreciation-focused lessons.

## Router Inputs

The router must inspect or infer:

- lesson position in unit;
- unit phase role;
- practice intensity;
- student work time ratio;
- teacher support density;
- performance task link;
- stage evidence link.

## Router Outputs

The router must influence:

- explanation density;
- demonstration density;
- number and depth of micro-practices;
- formal creation time;
- teacher circulation and observation focus;
- showcase and critique intensity;
- learning sheet fields;
- evidence collection mode.

## Required Fields

| Field | Required | Allowed values |
| --- | --- | --- |
| lesson_position_in_unit | yes | early / middle / late / final |
| unit_phase_role | yes | intro_understanding / technique_preparation / practice_creation / showcase_evaluation / transfer_closure / project_synthesis |
| practice_intensity | yes | low / medium / high |
| student_work_time_ratio | yes | low / medium / high |
| teacher_support_density | yes | light / normal / heavy |
| performance_task_link | yes | structured object |
| stage_evidence_link | yes | structured object |

## Router Guard

The router must prevent all lessons from becoming the same manuscript pattern.

It must explicitly support:

- low-practice understanding or appreciation lessons;
- technique preparation lessons with short trials and evidence records;
- practice creation lessons with heavy student work and teacher circulation;
- showcase / evaluation lessons with critique and reflection evidence;
- project synthesis lessons that connect multiple prior evidences.

## Current Decision

```text
R224A = PLANNING_CONTRACT_ONLY
NEXT_DECISION_TARGET = PASS_CONTINUE_TO_R224B_ROUTER_FIXTURE_AND_REGRESSION
```
