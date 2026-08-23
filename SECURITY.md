# Security Policy / Sicherheitsrichtlinie

## Reporting a Vulnerability / Sicherheitslücke melden

If you discover a security vulnerability or security concern within any repository in the `research-line` organization, please report it responsibly:

1. **Do NOT open a public issue** or disclose vulnerability details publicly before a fix is available.
2. Use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories) on the affected repository to create a private draft advisory.
3. Or contact the maintainers directly via email:
   - `security@open-bricks.org`
   - `security@ellmos.ai`
   - `lukas@open-bricks.org`
   - `support@lukasgeiger.com`

---

## Response Timeline / Reaktionszeit

- **Acknowledgment:** Within 48 hours (best effort, guaranteed within 7 days)
- **Initial Assessment & Triage:** Within 7 to 14 days
- **Fix & Disclosure Coordination:** Best effort, typically within 30 days depending on severity

---

## Supported Versions / Unterstützte Versionen

| Repository / Package | Supported Release | Security Updates |
|---|---|---|
| Active repositories (`functional-stability-theory`, `rh-even-dominance`, `abc-hct`, `crm-cosmology`, `fst-nash`, `ai-elite-swr`, `.github`) | Latest commit on `main`/`master` | :white_check_mark: Supported |
| Archived repositories (`rfep-framework`) | Historical reference / read-only | :x: End of Life / Historical Snapshot |

---

## Open Science Scope & Invariants / Sicherheitsinvarianten

- **Zero-Egress & Local-First:** All mathematical verification scripts, notebook computations, and rank certificate generators run 100% locally with zero unconsented telemetry or data egress.
- **Unprivileged User Mode (Non-Elevation):** None of the research software tools require elevated administrator/root permissions.
- **Reproducible Open Data:** Open-science datasets and Zenodo snapshots are cryptographically referenced and verified against integrity checksums.
