# R223Z HTML Artifact Policy

stage_id: 1013R_R223Z_LINE_CLOSURE_AND_NEXT_STAGE_PLANNING

## Locked Rule

HTML artifacts are allowed only in two cases:

1. Teacher manuscript pages.
   - They belong to R223M / R223N / R223O manuscript lines.
   - They must be mature teacher-readable teaching design manuscripts.

2. Explicitly authorized UI / workbench mock pages.
   - They require separate UI-line authorization.
   - Current formal UI and R97B remain blocked.

## HTML Is Not Allowed For

- gate review;
- ledger review;
- schema review;
- field review;
- safety flag review;
- component trigger metadata review;
- review-only pilot gate packages;
- sandbox reduction decisions.

## Sandbox Rule

Sandbox / review shell artifacts must not generate new teacher drafts, must not become teacher manuscript baselines, and must not compete with the canonical M/N/O teacher manuscripts.

## Enforcement

Future validators for gate / ledger / schema / safety packages should fail if unexpected `.html` artifacts appear.
