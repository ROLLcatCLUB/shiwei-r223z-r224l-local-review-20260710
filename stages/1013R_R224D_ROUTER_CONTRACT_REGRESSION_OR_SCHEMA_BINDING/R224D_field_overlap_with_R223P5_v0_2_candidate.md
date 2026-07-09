# R224D Field Overlap With R223P-5 v0.2 Candidate

stage_id: 1013R_R224D_ROUTER_CONTRACT_REGRESSION_OR_SCHEMA_BINDING

## Router Input Fields

| R224C field | R223P-5 status | Binding decision |
| --- | --- | --- |
| unit_phase_role | Existing general pedagogy core candidate | Reuse existing field |
| lesson_position_in_unit | Existing general pedagogy core candidate | Reuse existing field |
| practice_intensity | Existing general pedagogy core candidate | Reuse existing field |
| student_work_time_ratio | Existing general pedagogy core candidate | Reuse existing field |
| teacher_support_density | Existing general pedagogy core candidate | Reuse existing field |
| performance_task_link | Existing general pedagogy core candidate | Reuse existing field |
| stage_evidence_link | Existing general pedagogy core candidate | Reuse existing field |
| router_effect | Not a R223P-5 standalone field | Do not add as monolithic required schema field |

## Event Expansion Fields

| R224C event field | R223P-5 status | Binding decision |
| --- | --- | --- |
| event_count_bias | Derived effect, not existing schema field | Ledger-only or computed planning output |
| explanation_density | Derived effect, not existing schema field | Optional event planning metadata, hidden from teacher default |
| demonstration_density | Overlaps with demonstration_type but not identical | Map to demonstration_type plus optional density note |
| micro_practice_count | Overlaps with micro_practice_type but not identical | Optional derived count, not replacement for micro_practice_type |
| formal_creation_time | Derived effect, not existing schema field | Optional planning metadata |
| teacher_circulation_focus | Related to checkpoint / teacher support | Naturalize in manuscript, ledger trace optional |
| showcase_evaluation_intensity | Related to showcase_evaluation rules / evidence_outputs | Optional planning metadata |
| learning_sheet_fields | Existing review-ledger-only field | Reuse ledger-only field |
| evidence_collection_mode | Related to evidence_trigger.details / process_evidence / stage_evidence_link | Map to evidence fields, no new required field |
| checkpoint | Existing general pedagogy candidate field | Reuse existing field |
| exit_condition | Existing general pedagogy candidate field | Reuse existing field |

## No Conflict Findings

No direct naming conflict was found between R224C router inputs and R223P-5 candidate fields.

The main risk is over-promoting derived effect fields into formal schema. R224D recommends keeping them as computed contract outputs, ledger metadata, or optional event planning metadata until further regression.
