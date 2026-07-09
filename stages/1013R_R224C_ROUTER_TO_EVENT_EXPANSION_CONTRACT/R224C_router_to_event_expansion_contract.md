# R224C Router To Event Expansion Contract

stage_id: 1013R_R224C_ROUTER_TO_EVENT_EXPANSION_CONTRACT
status: CONTRACT_ONLY

## Purpose

R224C defines how `unit_lesson_practice_intensity_router` output changes `classroom_event_expansion`.

R224A defined the router. R224B proved the router changes sample density. R224C now defines the transmission contract:

```text
unit lesson router
-> classroom event expansion density and field values
-> teacher default manuscript rhythm
-> review ledger trace
-> screen / learning sheet / evidence rules
```

R224C does not modify R223M/N/O teacher manuscripts, does not publish v0.2, does not create HTML, and does not start UI/R97B/runtime/model/prompt/db work.

## Contract Principles

1. Router values must change event expansion before the teacher manuscript is rendered.
2. Teacher default manuscript must not display raw router field names.
3. Review ledger must preserve router fields and source/evidence status.
4. Screen, learning sheet, and evidence triggers must follow unit phase role and practice density.
5. High support does not mean high whole-class explanation.
6. Low practice does not mean low teaching value.

## Event Density By Unit Phase Role

| unit_phase_role | Event density | Main classroom emphasis |
| --- | --- | --- |
| intro_understanding | few, clear events | observe, compare, name, understand, express |
| technique_preparation | medium events | demonstrate, try, compare method, record evidence |
| practice_creation | creation-serving events | protect making time, circulate, rescue, collect process evidence |
| showcase_evaluation | critique/evidence events | explain work, peer/self evaluate, collect assessment evidence |
| transfer_closure | synthesis events | transfer, connect to life/use/performance task, close unit thread |
| project_synthesis | coordinated events | assemble prior evidence, complete performance product, present rationale |

## Affected Classroom Event Fields

Router output must affect at least:

- explanation_density;
- demonstration_density;
- micro_practice_count;
- formal_creation_time;
- teacher_circulation_focus;
- showcase_evaluation_intensity;
- learning_sheet_fields;
- evidence_collection_mode;
- checkpoint;
- exit_condition.

## Teacher Manuscript Transmission

The teacher manuscript should show the router effect as natural teaching rhythm:

- high practice -> less long explanation, more work time, circulation, rescue, and evidence;
- technique preparation -> demonstration, micro-practice, trial sample, method comparison;
- intro understanding -> observation, naming, comparison, short expression;
- showcase evaluation -> work explanation, evaluation language, assessment evidence;
- transfer closure -> migration, synthesis, unit performance task connection.

It must not show:

```text
unit_phase_role = ...
practice_intensity = ...
router_effect = ...
```

## Review Ledger Transmission

The review ledger must preserve:

- unit_phase_role;
- lesson_position_in_unit;
- practice_intensity;
- student_work_time_ratio;
- teacher_support_density;
- performance_task_link;
- stage_evidence_link;
- router_effect;
- source evidence / teacher assumption status.

## Decision Target

```text
PASS_CONTINUE_TO_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING
```
