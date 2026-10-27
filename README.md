# Northwind Portal Demo App

Internal reference application used by Northwind Digital to validate
Self-Service Automation Portal → Controller → cloud provision workflows.

This is **not** an Ansible collection. Application owners consume automation
from `northwind.cloud` / `northwind.platform` via portal job templates.

## Layout

- `src/` — minimal Flask health service
- `deploy/` — example Controller extra_vars / inventory notes
- `docs/` — runbook links for on-call

## Ownership

- Product: Digital Experience
- Ops: Cloud Operations (`cloud-ops@northwind.example`)
- Cost center: CC-2400
