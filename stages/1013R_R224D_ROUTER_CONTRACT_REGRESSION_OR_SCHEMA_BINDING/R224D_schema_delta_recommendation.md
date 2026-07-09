# R224D Schema Delta Recommendation

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING

## Recommendation

Do not publish a new schema version from R224D.

Do not add `router_effect` as a required schema object.

## Recommended Delta Status

| Field / concept | Recommendation |
| --- | --- |
| unit_phase_role | Already covered in R223P-5; no new field |
| lesson_position_in_unit | Already covered in R223P-5; no new field |
| practice_intensity | Already covered in R223P-5; no new field |
| student_work_time_ratio | Already covered in R223P-5; no new field |
| teacher_support_density | Already covered in R223P-5; no new field |
| performance_task_link | Already covered in R223P-5; no new field |
| stage_evidence_link | Already covered in R223P-5; no new field |
| router_effect | Keep as computed contract output, not formal required schema |
| event_count_bias | Candidate optional ledger/planning metadata |
| explanation_density | Candidate optional event planning metadata |
| demonstration_density | Candidate optional density note, maps to demonstration_type |
| micro_practice_count | Candidate optional count note, maps to micro_practice_type |
| formal_creation_time | Candidate optional planning metadata |
| teacher_circulation_focus | Candidate ledger note / checkpoint support |
| showcase_evaluation_intensity | Candidate optional planning metadata |
| learning_sheet_fields | Existing review-ledger-only field |
| evidence_collection_mode | Candidate ledger note mapped to evidence fields |
| checkpoint | Existing R223P-5 field |
| exit_condition | Existing R223P-5 field |

## Next Step

R224D can pass to R224E only as a candidate lock / binding confirmation step, not as formal v0.2 publication.
