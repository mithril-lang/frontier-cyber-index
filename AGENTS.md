# AGENTS.md — mithril-lang/frontier-cyber-index

- Purpose: Mithril Frontier Cybersecurity Index (MFCI): evaluation design and public educational measurements.
- Owner: Platform Engineering (Jun Kawasaki, @com-junkawasaki).
- Visibility: public. Do not change it without Jun's GO.
- Separate-repository reason: Public dataset and evaluation design (policy section 4, reason 3).
- Verification: `python3 scripts/test_catalog.py` and `python3 scripts/test_measurement.py`.
- Release path: No deployment. `analysis.mithril.fund` (mithril-fund `apps/analysis`) pins a dataset commit.

Rules: merge with a merge commit (no squash or rebase). Never commit secrets,
customer data or real target details. Run `gitleaks git --redact` before
pushing when it is installed.

Repository rules and classification: [mithril-fund repository policy](https://github.com/mithril-lang/mithril-fund/blob/main/docs/operations/repository-policy.md)
(`docs/operations/repository-policy.md` in mithril-fund).
