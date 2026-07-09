# 1013R_R224I Router To Classroom Event Expansion Field Convergence Static Precheck

Status: `LOCAL_REVIEW_PACKAGE`

This package is a non-visual static precheck. It checks whether the `unit_lesson_practice_intensity_router` standard candidate can converge with `classroom_event_expansion` fields without turning `router_effect` into a new required schema object.

## Decision

```text
R224I = PASS_FIELD_CONVERGENCE_STATIC_PRECHECK
NEXT_ALLOWED = R224J_OR_HOLD_DECISION_BY_REVIEWER
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

## What This Package Checks

1. Router input fields still reuse the R223P-5 candidate fields:
   - `unit_phase_role`
   - `lesson_position_in_unit`
   - `practice_intensity`
   - `student_work_time_ratio`
   - `teacher_support_density`
   - `performance_task_link`
   - `stage_evidence_link`
2. `router_effect` is not a required schema object.
3. `router_effect` only acts as a computed bridge toward classroom event expansion.
4. Three samples are checked:
   - `红红的剪纸` as `technique_preparation_unit`
   - `寓言与神话` as `project_synthesis_unit`
   - `美术大家庭` as `appreciation_intro_understanding_unit`
5. Teacher default text must not leak raw router fields.
6. Review ledger trace must remain available for audit.

## Boundaries

```text
No HTML
No R97B
No frontend/backend
No runtime/provider/model
No prompt change
No database
No lesson body writeback
No R222D component library modification
No R223M/N/O teacher manuscript modification
No formal apply
No v0.2 publication
```

## Files

- `R224I_field_convergence_static_precheck_report.md`
- `R224I_router_to_event_expansion_mapping_matrix.json`
- `R224I_required_schema_object_leak_check.md`
- `R224I_teacher_default_visibility_check.md`
- `R224I_review_ledger_trace_check.md`
- `R224I_publication_status_notice.md`
- `R224I_validator_result.json`
- `validate_1013R_R224I_router_to_classroom_event_expansion_field_convergence_static_precheck.py`
- `PACKAGE_MANIFEST.json`

