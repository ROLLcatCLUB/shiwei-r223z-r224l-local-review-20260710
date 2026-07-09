# R224F Extra Unit Regression Report

stage_id: 1013R_R224F_ROUTER_STANDARD_EXTRA_UNIT_REGRESSION
status: EXTRA_UNIT_REGRESSION_ONLY

## Purpose

R224F validates the R224E `unit_lesson_practice_intensity_router` standard candidate on three additional unit structures.

It does not publish v0.2, does not create teacher manuscripts, does not create HTML, and does not start UI/R97B/runtime/model/prompt/db work.

## Source Standard Candidate

```text
R224E = PASS_LOCK_UNIT_ROUTER_STANDARD_CANDIDATE
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

## Additional Regression Samples

| Regression sample | Unit structure type | Router stress point |
| --- | --- | --- |
| 红红的剪纸 | technique_preparation | Can the router keep technique preparation from becoming a full final-product pressure lesson? |
| 寓言与神话 | project_synthesis | Can the router support integrated project synthesis and evidence assembly? |
| 美术大家庭 | intro_understanding | Can the router keep appreciation / cognition / introduction lessons from being misread as high-practice lessons? |

## Regression Result

```text
R224F = PASS_LOCAL_PENDING_REVIEW
router_input_fields_reused_from_R223P5 = true
router_effect_required_schema_object = false
teacher_visibility_leak = false
review_ledger_trace = pass
v0_2_published = false
```

## Main Finding

The router candidate remains stable across additional unit structures:

- technique preparation routes toward demonstration, short practice, method evidence, and safety/management;
- project synthesis routes toward assembling prior evidence, product completion, rationale presentation, and evaluation;
- intro understanding routes toward observation, classification, comparison, and light evidence rather than heavy making.

## Boundary

```text
No HTML.
No R97B.
No frontend/backend.
No runtime/provider/model.
No prompt change.
No database.
No lesson body writeback.
No R222D component library modification.
No M/N/O teacher manuscript modification.
No formal apply.
No v0.2 publication.
```

## Decision Target

```text
PASS_CONTINUE_TO_R224G_ROUTER_STANDARD_REGRESSION_SUMMARY_OR_HOLD
```
