# R224G Publication Hold Rationale

stage_id: 1013R_R224G_ROUTER_STANDARD_REGRESSION_SUMMARY_OR_HOLD

## Decision

```text
PASS_SUMMARY_READY_AND_HOLD_PUBLICATION
```

## Hold Reason

R224E and R224F are sufficient to summarize the router candidate and preserve it for future review. They are not sufficient to publish `R223M_STANDARD_V0_2`.

## Missing Before Publication

### 1. True generated teacher manuscript leakage regression

The router fields must be tested against actual teacher default manuscript output to verify that raw fields do not leak into the teacher-facing text.

### 2. classroom_event_expansion formal field convergence

R224C/D/E distinguish router inputs, computed outputs, optional event metadata, and ledger-only fields. Formal field convergence is still pending.

### 3. UI / R97B readiness

Formal UI and R97B remain blocked. Router publication should not be used as a backdoor to product UI.

### 4. Cross-grade real unit pressure test

Current samples cover multiple unit structures, but not enough grade-level diversity.

### 5. Long-unit / short-unit stress test

The router must still prove stable across units with very different length and performance task depth.

## Publication Status

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
```

This remains true after R224G.
