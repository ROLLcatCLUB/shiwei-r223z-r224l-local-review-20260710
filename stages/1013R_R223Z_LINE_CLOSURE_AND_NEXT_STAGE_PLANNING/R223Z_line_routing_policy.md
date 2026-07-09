# R223Z Line Routing Policy

stage_id: 1013R_R223Z_LINE_CLOSURE_AND_NEXT_STAGE_PLANNING

## Four Lines After R223

Future work must route to one of these four lines. Do not continue a mixed R223 chain.

## 1. Teacher Manuscript Quality Line

Route:

```text
教师稿质量问题 -> R223M / R223N / R223O
```

Examples:

- the teacher manuscript reads unnaturally;
- the classroom process is not sufficiently expanded;
- design intent is too heavy or too thin;
- sample flavor is missing;
- manuscript layout does not feel like a mature teaching design.

Allowed artifact type:

- teacher manuscript md/html only inside the corresponding manuscript line.

## 2. v0.2 Field / Schema / Ledger Line

Route:

```text
v0.2 字段 / schema / ledger 问题 -> R223P / R223Q
```

Examples:

- candidate schema field is unclear;
- review ledger cannot trace evidence;
- v0.2 candidate fields overfit one sample;
- regression fixtures fail.

Allowed artifact type:

- md/json/checklist/validator/review ZIP.

## 3. Sandbox / Gate Review Line

Route:

```text
sandbox / gate 审核问题 -> md / json / checklist / validator
```

Examples:

- safety flags are unclear;
- v0.1/v0.2 difference summary is too heavy;
- component trigger metadata is ambiguous;
- gate acceptance / hold conditions conflict.

Allowed artifact type:

- non-visual review package only.

HTML is not allowed by default.

## 4. Formal UI / R97B Line

Route:

```text
正式 UI / R97B 问题 -> BLOCKED until separately authorized
```

Formal UI, R97B route/component/CSS, runtime, provider/model, prompt, database, writeback, and formal apply remain blocked.

## Routing Guard

If an issue touches more than one line, create a routing note first. Do not fix it by creating a new static page.
