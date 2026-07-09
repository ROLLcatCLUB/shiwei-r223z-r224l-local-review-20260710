# 1013R_R224J Cross Grade And Unit Length Pressure Static Regression

Status: `LOCAL_REVIEW_PACKAGE`

This package is a non-visual static regression package. It checks whether the `unit_lesson_practice_intensity_router` standard candidate remains stable across grade bands and unit length types.

## Decision

```text
R224J = PASS_CROSS_GRADE_AND_LENGTH_STATIC_REGRESSION
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

## Scope

This package checks:

1. Cross-grade pressure:
   - low grade observation / game / simple material experience
   - middle grade technique preparation / small project creation
   - high grade design application / integrated expression
2. Unit-length pressure:
   - single-lesson short task
   - two-lesson progression
   - multi-lesson project
3. Router input fields remain limited to the R223P-5 candidate set.
4. `router_effect` remains computed bridge metadata, not a required schema object.
5. Teacher default implications are naturalized and do not leak raw router fields.
6. Review ledger trace remains available.

## Boundary

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

- `PACKAGE_MANIFEST.json`
- `R224J_cross_grade_and_unit_length_pressure_report.md`
- `R224J_cross_grade_pressure_matrix.json`
- `R224J_unit_length_pressure_matrix.json`
- `R224J_teacher_default_visibility_check.md`
- `R224J_review_ledger_trace_check.md`
- `R224J_publication_status_notice.md`
- `R224J_validator_result.json`
- `validate_1013R_R224J_cross_grade_and_unit_length_pressure_static_regression.py`

