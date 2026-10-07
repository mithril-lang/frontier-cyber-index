# Cybersecurity exercises that follow industry workflows

2026-10-07. Introducing the MFCI v0.1 design and public educational materials. No model scores have been measured yet.

A solved cybersecurity challenge needs a connection to the work it protects. Finance teams must keep authorized payments running while holding unapproved changes. Healthcare teams must preserve care and patient privacy. Manufacturing teams must maintain safety and monitoring. Mithril has organized coverage by industry, technical surface, and workflow to put those constraints into the evaluation from the beginning.

## Learn from competitions and add business constraints

The DEF CON 33 rules combine attack and defense with patching and service continuity. The 2026 Cloud Village covers cloud and IAM topics, while Black Hat training evaluations include CTF, practical, scenario, and project formats. These inform our design; we do not reproduce their challenges or combine their scores. [DEF CON 33 rules](https://nautilus.institute/files/rules-2025-100.pdf), [Cloud Village 2026](https://www.cloud-village.org/dc34), [Black Hat training exams](https://blackhat.com/html/certificates.html).

Our exercises have three stages. A asks participants to distinguish suspicious, normal, and inconclusive evidence. B asks them to repair source or configuration while preserving legitimate activity. C introduces incomplete evidence over time and asks for decisions about holding, isolating, continuing, and restoring operations. Recovery includes checking ledger and permission consistency.

## Define the coverage denominator first

Our initial taxonomy contains 24 industry views and 18 technical surfaces. It uses the [NIST glossary's 16 US critical infrastructure categories](https://csrc.nist.gov/glossary/term/critical_infrastructure_sectors) as a reference and adds education, ecommerce, media, hospitality, professional services, real estate, crypto assets, and AI services. These categories overlap. They are not a universal classification or a complete mapping to Japan's infrastructure framework.

The repository contains 72 industry scenario specifications, 18 cross-industry specifications, and eight offline exercises. Specifications, working educational fixtures, and independently verified model measurements have separate coverage. Naming 24 industries and 18 surfaces does not mean all 432 intersections have been tested. The [coverage register](https://github.com/mithril-lang/frontier-cyber-index/blob/main/catalog/coverage.json) also shows the gaps.

## Evaluate continuity as well as protection

| Industry | Initial exercise | What must continue |
| --- | --- | --- |
| Finance | Voice-requested bank detail changes | Authorized payments and independent approval |
| Healthcare | Emergency access and audit | Care, patient separation, and recorded grants |
| Manufacturing | Expired maintenance access | Safety, asset scope, and monitoring |
| IT/SaaS | Tenant authorization and OAuth | Customer isolation and legitimate synchronization |
| Logistics | Modified and repeated webhooks | Exactly-once application and ledger consistency |
| Media | Consent and disclosure for synthetic video | Revocation handling and provenance review |

These are original fictional scenarios, not reconstructions of actual incidents. A system cannot earn a high score by denying everything. We also report legitimate completion, false positives, evidence gaps, costs, and time. MFCI defensive capability D, offensive capability O, and safety S remain separate. The planned Mithril comparison uses the same model and tasks in paired configurations.

## Start with the exercises and inspect the gaps

The [repository](https://github.com/mithril-lang/frontier-cyber-index) includes synthetic evidence, answer templates, a grader, and public reference answers. No network access or real person's voice or video is needed. The eight L0 exercises teach evidence-based decisions; they do not replace code repair or extended cyber ranges. Positive and negative grader controls establish educational behavior, not frontier capability.

Next come industry expert review, execution environments, independent hidden graders, private holdouts, and human baselines. Read the [industry catalogue](https://github.com/mithril-lang/frontier-cyber-index/blob/main/docs/INDUSTRY-CATALOG.md) to identify the business constraints missing from your scenario. The [AI video and agent report](https://github.com/mithril-lang/frontier-cyber-index/blob/main/reports/EMERGING-TECH-MISUSE-2026-10-07.md) separates sourced observations from Mithril's analysis.
