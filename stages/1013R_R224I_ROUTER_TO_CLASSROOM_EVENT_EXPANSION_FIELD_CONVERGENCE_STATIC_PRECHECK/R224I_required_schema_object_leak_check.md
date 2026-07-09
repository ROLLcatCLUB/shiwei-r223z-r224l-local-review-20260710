# R224I Required Schema Object Leak Check

## Result

```text
required_schema_object_leak = false
router_effect_required_schema_object = false
```

## Check

R224I does not promote `router_effect` into a required saved schema object. It remains a computed bridge that can be derived from the existing router input fields and summarized in the review ledger.

Allowed use:

```text
router input fields
→ computed router_effect summary
→ classroom_event_expansion bias / density hints
→ teacher-facing naturalized implication
```

Blocked use:

```text
router_effect as required classroom_event_expansion schema object
router_effect as teacher-default raw field group
router_effect as v0.2 published field
router_effect as lesson body writeback object
```

## Reason

The current R223P-5 / R224E standard candidate already has enough input fields to decide lesson position, phase role, practice intensity, work-time ratio, teacher support density, performance task link, and stage evidence link. R224I only confirms how those values should affect event expansion density.

