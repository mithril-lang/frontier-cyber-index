# AI video, voice impersonation, and authority boundaries

2026-10-07. A review of public primary sources, not an allegation of misconduct or a discovered vulnerability at a provider.

A familiar face and voice on a video call do not establish who authorized a payment or document release. Real-time AI video and audio can also connect to retrieval and business tools. Mithril reviewed provider capabilities, reported misuse, and the boundaries adopters should test separately.

## What we verified about Tavus

Tavus describes Phoenix-4.5 rendering, Raven-1 audiovisual perception, and Sparrow-2 conversational flow. Its [engineering documentation](https://github.com/Tavus-Engineering/tavus-intake/blob/main/docs/tavus-features.md) shows a configuration that handles persona tool calls during a conversation. We checked the [product description](https://www.tavus.io/), but did not measure performance or the accuracy of emotion inference.

The [Acceptable Use Policy](https://www.tavus.io/acceptable-use-policy), effective April 14, 2026, requires explicit consent, AI disclosure, and respect for consent revocation, among other requirements. A published requirement is separate from a measured prevention rate. We did not bypass Tavus's consent checks or clone real people without permission.

## Separate observed misuse from provider attribution

The FBI/IC3 warned about financial fraud using generated audio and video in December 2024. Its May 2025 warning describes AI voice impersonation of senior US officials beginning that April. Neither establishes that Tavus was used. [Generative AI fraud warning](https://www.ic3.gov/PSA/2024/PSA241203), [official impersonation warning](https://www.ic3.gov/PSA/2025/PSA250515).

[Anthropic's September 2026 report](https://www.anthropic.com/threat-intelligence-report-september-2026) describes cases involving cyber operations, scams, and other misuse, covering December 2025 through August 2026. This is a provider's observation of selected cases, not a measurement of market-wide prevalence or every model's capability.

## Separate appearance, authentication, and transaction approval

The following is Mithril's threat analysis. Treating video or voice as the only identity check could enable unverified bank-detail changes, MFA recovery, or confidential document requests. Test a previously registered independent contact route, the authenticated principal, and approval bound to the actual operation: which recipient, which document, which account, and what amount.

| Boundary | What the exercise checks |
| --- | --- |
| Face or voice to identity | Similarity does not authorize an exception |
| Document or conversation to tool | Untrusted content cannot expand permission |
| Consent to replica use | Purpose, expiry, and revocation remain effective |
| Recording or perception to storage | Access and retention are limited; uncertain inferences remain uncertain |
| Approval to execution | The operation matches approval; refusals and successful actions are recorded |

A deepfake detector alone cannot establish identity. Provenance also does not guarantee that a statement is true or that the speaker can authorize a transaction. Missing provenance does not prove a fake. Evidence retention and legitimate task completion must be tested together.

## Measure conversational agents in business workflows

[OWASP's September 2026 announcement](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) introduces updated LLM guidance and the Agent Control Standard, among other resources. Mithril plans to use these references when testing runtime authority and legitimate completion alongside prompt-level guidance.

Our [educational exercises](https://github.com/mithril-lang/frontier-cyber-index/tree/main/exercises) cover voice-requested bank changes, consent revocation, and documents that try to alter tool authority. All evidence is fictional. Real likenesses and financial transactions are unnecessary. These introductory fixtures do not certify Tavus's controls or frontier model performance.

Read the [report and source register](https://github.com/mithril-lang/frontier-cyber-index/tree/main/reports), then identify where your workflow checks identity, approves an operation, and honors consent revocation. Mithril will publish measured results after independent graders and private tasks are ready.
