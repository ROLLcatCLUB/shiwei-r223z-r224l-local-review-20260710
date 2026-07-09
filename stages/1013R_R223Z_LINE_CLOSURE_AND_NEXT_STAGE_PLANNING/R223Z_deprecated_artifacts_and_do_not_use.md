# R223Z Deprecated Artifacts And Do Not Use List

stage_id: 1013R_R223Z_LINE_CLOSURE_AND_NEXT_STAGE_PLANNING

## Deprecated Or Rescoped

| Artifact / route | Status | Do not use as |
| --- | --- | --- |
| R223X static HTML fixture | DEPRECATED_AS_REVIEW_MAIN_ARTIFACT | Teacher page, UI baseline, manuscript baseline, review main artifact |
| R223Y teacher walkthrough | CANCELLED_OR_RESCOPED | Next default step |
| Sandbox shell pages | REVIEW_SHELL_ONLY | Teacher manuscript source of truth |

## Do Not Use Rules

1. R223X static HTML must not be used as a teacher-facing teaching design page.
2. R223X static HTML must not be used as a R97B carrier proposal.
3. R223X static HTML must not be used as a manuscript baseline.
4. R223Y must not proceed as teacher walkthrough unless explicitly rescoped.
5. Gate / ledger / schema / field / safety review must not generate HTML pages.
6. Sandbox shell artifacts must not become final teacher pages.
7. Review ledger must not be exposed as teacher default reading.
8. Component trigger metadata must not be interpreted as executable classroom component controls.

## Replacement Rule

Use non-visual review packages for:

- schema review;
- ledger review;
- gate review;
- field review;
- safety flag review;
- component trigger metadata review.

Use HTML only for:

- canonical teacher manuscript pages;
- explicitly authorized UI / workbench mock pages.
