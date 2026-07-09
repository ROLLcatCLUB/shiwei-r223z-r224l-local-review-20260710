# R224G Router Standard Regression Summary Or Hold

stage_id: 1013R_R224G_ROUTER_STANDARD_REGRESSION_SUMMARY_OR_HOLD
status: SUMMARY_READY_AND_PUBLICATION_HOLD

## Purpose

R224G summarizes the R224E unit router standard candidate lock and R224F extra unit regression. It decides whether the router candidate is ready for publication or should remain held.

R224G does not add new functionality, does not publish `R223M_STANDARD_V0_2`, does not create HTML, and does not start UI/R97B/runtime/model/prompt/db work.

## R224E Summary

R224E locked the unit lesson practice intensity router as a standard candidate:

- router input fields reuse R223P-5;
- `router_effect` is not a required schema object;
- router_effect is not a required schema object;
- `router_effect` is computed contract output and review ledger summary;
- teacher default manuscript does not display raw router fields;
- review ledger preserves router trace;
- `R223M_STANDARD_V0_2 = NOT_PUBLISHED`.

## R224F Summary

R224F added three unit structure regression samples:

- 红红的剪纸: `technique_preparation_unit`;
- 寓言与神话: `project_synthesis_unit`;
- 美术大家庭: `appreciation_intro_understanding_unit`.

The added regression supports that the router can distinguish:

- technique preparation from final product pressure;
- project synthesis from single technique practice;
- appreciation / intro understanding from high-intensity making.

## Current Coverage

The router candidate currently covers:

- technique preparation;
- project synthesis;
- appreciation / introduction / understanding;
- practice intensity differences;
- teacher support density differences;
- student work time ratio differences;
- teacher default visibility guard;
- review ledger trace.

## Publication Decision

```text
R224G = PASS_SUMMARY_READY_AND_HOLD_PUBLICATION
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

## Why Hold Publication

The candidate is stable enough for summary and future review, but not enough for formal publication.

Remaining gaps:

1. teacher default manuscript leakage regression is not yet run on true generated manuscripts;
2. classroom_event_expansion formal field convergence is not yet complete;
3. UI / R97B is still blocked;
4. cross-grade real unit pressure tests are not done;
5. long-unit / short-unit differences are not yet stress-tested.

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
