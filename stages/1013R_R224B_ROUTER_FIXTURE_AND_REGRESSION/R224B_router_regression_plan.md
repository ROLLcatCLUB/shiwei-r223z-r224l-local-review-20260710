# R224B Router Regression Plan

stage_id: 1013R_R224B_ROUTER_FIXTURE_AND_REGRESSION
status: ROUTER_FIXTURE_AND_REGRESSION_ONLY

## Purpose

R224B validates whether `unit_lesson_practice_intensity_router` changes classroom event expansion density across three different art lesson samples.

It does not create new formal teacher manuscripts, does not modify R223M/N/O teacher manuscripts, does not publish v0.2, and does not start UI/R97B/runtime/model/prompt/db work.

## Regression Question

```text
Do the router values change the generated classroom event expansion expectations in a visible and pedagogically meaningful way?
```

## Samples

| Sample | Router profile | Expected expansion bias |
| --- | --- | --- |
| 我为文具代言 | late / practice_creation / high / high / heavy | Longer creation time, less whole-class explanation, heavier circulation support and process evidence |
| 有趣的纸印 | middle / technique_preparation / medium / medium / normal | Controlled material observation, demonstration, trial samples, method comparison, modest final work |
| 色彩的碰撞 | early / intro_understanding / medium / medium / normal | Life color observation, color-mixing micro-practice, color language expression, not heavy creation |

## Required Checks

1. Three sample router values are complete.
2. Density effects differ across samples.
3. High-practice sample is not over-explained.
4. Technique-preparation sample is not turned into a heavy finished-product lesson.
5. Intro-understanding sample is not turned into a heavy creation lesson.
6. Teacher default view hides router field names.
7. Review ledger may keep router fields.
8. Existing R223M/N/O teacher manuscripts are not modified.
9. v0.2 is not published.
10. UI/R97B/runtime remain blocked.

## Decision Target

```text
PASS_CONTINUE_TO_R224C_ROUTER_TO_EVENT_EXPANSION_CONTRACT
```
