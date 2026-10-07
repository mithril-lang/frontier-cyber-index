# Mithril Frontier Cybersecurity Index (MFCI)

A proposed evaluation framework for measuring frontier AI cybersecurity
capabilities, defensive task completion, agent safety, and the effect of
Mithril's policy and evidence infrastructure.

**Status: design proposal, v0.1. No benchmark runs or measured scores are published yet.**

## Evaluation axes

| Axis | Measures |
| --- | --- |
| **MFCI-D /100** | Evidence-backed defensive task completion: discovery, validation, repair, detection and response, cloud and identity, investigation |
| **MFCI-O /100** | Offensive capability on authorized isolated targets |
| **MFCI-S** | Prompt injection outcomes, authority boundaries, legitimate task completion, and evidence integrity |
| **ΔMithril** | Paired comparisons of the same model with and without Mithril |
| **Efficiency** | Success rates against total cost and elapsed time |
| **Evidence** | Traceability, independent verification, and reproducibility |

These axes remain separate. Offensive capability is not a safety score.

## Design specification

Read the [full design in Japanese](DESIGN.md) for scoring rules, task-family
aggregation, confidence intervals, comparison tracks, resource budgets,
grader controls, evidence contracts, and the initial pilot plan.

The proposed pilot covers six defensive domains with 20 task families each
and three repeats per task. Its results will inform the sample size for a
qualified release. The weights and budgets are proposals to freeze before
measurement.

## Current contents

This repository contains the design specification. The execution harness,
task datasets, graders, run receipts, and public leaderboard are planned work.
There is currently no benchmark command to run.

## Contributing

Use issues and pull requests to propose improvements to task validity,
scoring, reproducibility, statistical methods, or evaluation coverage.
Do not submit credentials, private production data, or details of undisclosed
vulnerabilities in public issues.

## Reference benchmarks

- [Cybench / AISI Inspect Cyber](https://inspect.cyber.aisi.org.uk/cybench.html)
- [CyberGym](https://github.com/sunblaze-ucb/cybergym)
- [CVE-Bench](https://arxiv.org/abs/2503.17332)
- [CyberSecEval 3](https://arxiv.org/abs/2408.01605)

MFCI is an independent design. Upstream benchmark scores and modified or
subset runs must be labeled separately from MFCI measurements.
