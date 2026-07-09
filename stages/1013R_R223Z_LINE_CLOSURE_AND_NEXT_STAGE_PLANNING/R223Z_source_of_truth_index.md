# R223Z Source Of Truth Index

stage_id: 1013R_R223Z_LINE_CLOSURE_AND_NEXT_STAGE_PLANNING

## Canonical Teacher Manuscripts

| Sample | Source of truth file | Line | Edit route |
| --- | --- | --- | --- |
| 我为文具代言 | R223M_P4_P1_teacher_readable_process_v6.html | R223M manuscript line | Return to R223M |
| 有趣的纸印 | R223N_P3_P1_teacher_manuscript_draft_v5.html | R223N manuscript line | Return to R223N |
| 色彩的碰撞 | R223O_P1_teacher_manuscript_draft_v2.html | R223O manuscript line | Return to R223O |

These three files are the canonical teacher-facing manuscript baselines. Sandbox / gate packages may reference them but must not rewrite, summarize as replacement, re-layout as final page, or create a fourth teacher manuscript baseline.

## Standard Source Of Truth

| Artifact | Source of truth | Status |
| --- | --- | --- |
| Classroom event expansion standard v0.1 | R223M-P5 | LOCKED_AS_CANDIDATE |
| R223M standard v0.2 candidate | R223P-5 | CANDIDATE_LOCKED_NOT_PUBLISHED |
| True generation regression gate | R223Q | PASS |
| v0.2 pilot route planning | R223R | PASS |
| Opt-in sandbox route spec | R223S | PASS |
| Sandbox preview / review / reduction decisions | R223T / R223U / R223V | PASS |
| Review-only pilot gate spec | R223W | PASS |
| Non-visual gate package rule | R223X-P1 | PASS |

## Active Status

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI = BLOCKED
R97B_ROUTE = BLOCKED
runtime/provider/model/prompt/db = BLOCKED
lesson body writeback = BLOCKED
formal apply = BLOCKED
```

## Source Of Truth Rule

If a later artifact conflicts with this index, the conflict must be resolved before any downstream planning proceeds.
