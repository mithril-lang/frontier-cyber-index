# Publication receipt — 2026-10-07

Status checked at **2026-10-07 02:48 UTC / 11:48 JST**.

## Public research repository

The coverage plan, 72 industry scenario specifications, 18 cross-industry
specifications, eight offline exercises, report, source register, and authored
Japanese/English blog sources are published on this repository's `main`.
Four catalogue/grader test groups passed again at 02:42 UTC.
**No verified frontier model runs, measured model scores, or rankings exist.**
The declared industry × technical-surface coverage is 72 of 432 cells (16.7%).
The eight exercises are educational fixtures with public reference answers.

## Mithril Analysis — live

[analysis.mithril.fund](https://analysis.mithril.fund/) is live, with an
[English overview](https://analysis.mithril.fund/en/), industry filters,
methodology, exercise evidence, research, source register, and downloadable data.
Detailed specifications and the research report are currently Japanese; this
language limitation is stated on the English pages.

Implementation was merged through [PR #563](https://github.com/mithril-lang/mithril-fund/pull/563)
and the custom-domain bootstrap correction through [PR #568](https://github.com/mithril-lang/mithril-fund/pull/568).
The successful [Analysis release](https://github.com/mithril-lang/mithril-fund/actions/runs/37562160809)
used code commit `ba582cb596df1bf7338d3ed7c06aa2c2da8579ce` and completed at
**02:30:42 UTC / 11:30:42 JST**. The deployed Worker version is
`b11c00a4-7d9f-471d-979e-0a14e1b813d2`.

The site pins research data commit `44e3701ccea1c162a77be298bbe8c10bbd54d2f0`;
subsequent README/publication receipts do not silently replace that snapshot.
The release verified custom-domain ownership, deployed version, bindings,
and exact public content/asset hashes. Five Analysis test groups passed;
78 static pages and 776 internal page/download links were checked.
Live browser checks covered Japanese/English navigation, mobile layout,
industry filtering/reset, and the research attribution caveat, with no
browser console errors observed.

## Mithril blog — live

Article source was merged through [PR #554](https://github.com/mithril-lang/mithril-fund/pull/554)
as `1cb13cabb32d9aabdf1ddff22d374b6cc47f7698`.
Both articles are now publicly available in Japanese and English:

- [Industry exercises](https://blog.mithril.fund/frontier-cyber-industry-exercises?lang=ja)
  / [English](https://blog.mithril.fund/frontier-cyber-industry-exercises?lang=en)
- [Tavus and authority boundaries](https://blog.mithril.fund/tavus-ai-video-authority-boundaries?lang=ja)
  / [English](https://blog.mithril.fund/tavus-ai-video-authority-boundaries?lang=en)

The blog job in [public-site run 37562883089](https://github.com/mithril-lang/mithril-fund/actions/runs/37562883089)
succeeded for source `f11a949ab5ba858d8a6077bb04675442c46fa960`.
Its deployed version is `56f78ad0-2795-4780-ba4b-62cf180b721a` and public
build ID is `f11a949ab5ba-20261007024650`, verified through the public
build metadata and CI bundle hash smoke. Actual rendered article bodies,
Japanese/English Analysis header URLs, and the English article → Analysis
navigation were checked in the browser; no console errors were observed.

## Mithril apex link — source merged, production blocked

The Analysis researcher link is merged in the apex source, but is **not live**.
The same public-site run passed verification and blog/support publication,
but apex upload failed with Cloudflare error 10085:
`R2 bucket internal-security-nvd not found` in the active source account.
The apex receipt has no uploaded/deployed version; its recorded prior version
is `485496a0-fe47-45f1-8574-3f728d1446b5`.
Actual public researcher links still omit Analysis.

This is an existing storage-ownership blocker documented in Mithril Fund's
AGENTS.md: restore the source R2 or choose the zone migration before changing
production bindings. No replacement data origin, empty bucket, cross-account
binding change, manual deployment, or stale-commit release was introduced.
All releases used existing CI current-main, ownership, binding, rollback,
and public smoke gates. The apex link remains the outstanding publication item.
