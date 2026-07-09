# R224D Risk And Conflict Notes

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING

## Risk 1. Duplicating existing R223P-5 fields

Risk:

R224C router inputs may be re-added under new names.

Control:

Reuse existing R223P-5 fields for router inputs.

## Risk 2. Promoting router_effect too early

Risk:

`router_effect` becomes a required schema object and duplicates event expansion fields.

Control:

Keep `router_effect` as computed contract output and ledger summary until later regression justifies formalization.

## Risk 3. Teacher default field leakage

Risk:

Teacher manuscripts show raw fields such as `practice_intensity` or `event_count_bias`.

Control:

Teacher default visibility guard treats field leakage as rendering defect.

## Risk 4. Ledger loses source status

Risk:

Router values appear as facts without source/assumption distinction.

Control:

Review ledger must record source_evidence, system_inference, teacher_assumption, or teacher_confirmation_required.

## Risk 5. Schema binding becomes v0.2 publication

Risk:

Compatibility with v0.2 candidate is mistaken for formal release.

Control:

R223M_STANDARD_V0_2 remains NOT_PUBLISHED. R224D does not publish v0.2.

## Boundary

No R97B, no route, no frontend/backend, no runtime/provider/model, no prompt, no database, no lesson body writeback, no R223M/N/O edits, no R222D edits, no v0.2 publication, no HTML, no formal apply.
