# Example — Start / Stop

The user-facing control is intentionally minimal.

```text
checkpoint start
```

From that point, infer the logical role from context:
- shape the next checkpoint when planning/design is needed;
- implement the accepted checkpoint when delivery is requested;
- review repository evidence when verification/review is requested.

Do not ask the user to choose a role unless the request is genuinely ambiguous in a way repository/context inspection cannot resolve.

The mode persists across turns until:

```text
checkpoint stop
```

Stopping leaves the user's repository and artifacts untouched; it only ends the workflow behavior.
