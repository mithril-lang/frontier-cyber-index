# 一次資料の出典台帳

確認日: 2026-10-07（JST）。文章・問題・画像・解答を転載せず、独自の分析と架空教材を作成。
参照可能であることと、データ/問題の再配布許可は別。CTF原問の採用はlicense確認後の別工程。
ページの宣伝文句を測定済み性能として扱わない。公開日と事象期間を分ける。

| ID | 一次資料 | 日付・確認状態 | 本資料で使う範囲 |
| --- | --- | --- | --- |
| S01 | [NIST: critical infrastructure sectors](https://csrc.nist.gov/glossary/term/critical_infrastructure_sectors) | 2026-10-07本文確認 | PPD-21由来の米国16分類。世界共通の業界分類とは扱わない |
| S02 | [NIST CSF 2.0 release](https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework) | 2024-02、本文確認 | Govern/Identify/Protect/Detect/Respond/Recover |
| S03 | [NIST SP 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | 2023-09、本文確認 | OTの性能・信頼性・安全制約 |
| S04 | [NIST SP 800-82r4 initial public draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd) | 2026-09のplanning note経由で確認 | 改訂中。finalのr3と区別 |
| S05 | [HHS healthcare CPGs](https://hhscyber.hhs.gov/cybersecurity-performance-goals.html) | 本文確認 | 医療の業務継続・防御策の参考。法令適合の認定ではない |
| S06 | [DEF CON 33 finals rules](https://nautilus.institute/files/rules-2025-100.pdf) | 2025大会、PDF確認 | attack/defend、patch、サービス維持、LiveCTF等の形式 |
| S07 | [Cloud Village at DEF CON 34](https://www.cloud-village.org/dc34) | 2026-08-07〜09のイベント案内、本文確認 | cloud/IAM/DevOpsとCTF。研究abstractは独立検証と区別 |
| S08 | [OWASP CTF at DEF CON 34](https://ctf.owasp.org/) | 2026、本文確認 | villageの独立した競技。main CTFと混同しない |
| S09 | [Black Hat training exams](https://blackhat.com/html/certificates.html) | 2026案内、本文確認 | CTF・実技・scenario/project評価という形式 |
| S10 | [Black Hat USA 2026 industry summits](https://blackhat.com/html/press/2026-06-16.html) | 2026-06-16、本文確認 | healthcare/AI/finance等の業界視点 |
| S11 | [Tavus product site](https://www.tavus.io/) | 2026-10-07本文確認 | Phoenix-4.5/Raven-1/Sparrow-2の提供者による機能説明 |
| S12 | [Tavus Engineering intake documentation](https://github.com/Tavus-Engineering/tavus-intake/blob/main/docs/tavus-features.md) | 2026-10-07本文確認 | persona/tool eventと動画対話の構成例。全実装を監査したわけではない |
| S13 | [Tavus Acceptable Use Policy](https://www.tavus.io/acceptable-use-policy) | 発効2026-04-14、本文確認 | 明示的同意、AI開示、同意撤回等の提供者の要件 |
| S14 | [FBI/IC3: generative AI financial fraud](https://www.ic3.gov/PSA/2024/PSA241203) | 公開2024-12-03、本文確認 | 音声・動画等を用いる詐欺の一般的警告。Tavusへの帰属なし |
| S15 | [FBI/IC3: officials impersonated](https://www.ic3.gov/PSA/2025/PSA250515) | 公開2025-05-15、事象2025-04以降、本文確認 | AI音声によるなりすまし。Tavusへの帰属なし |
| S16 | [OWASP Agentic Applications Top 10 for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | 公開2025-12-09、本文確認 | agent権限・workflowのリスク領域 |
| S17 | [OWASP 2026 resource announcement](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) | 表示2026-09-01、本文dateline09-02、本文確認 | LLM Top10更新とAgent Control Standard。両日付を保持 |
| S18 | [OWASP LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | 2026、resourceページ本文確認 | 新版の存在と評価参照。未読PDFの詳細順位は転載しない |
| S19 | [Anthropic: September 2026 misuse report](https://www.anthropic.com/threat-intelligence-report-september-2026) | 公開09-10（index表示）、対象2025-12〜2026-08、本文確認 | 提供者観測のcyber operations/詐欺等。全体頻度の推定ではない |
| S20 | [NIST AML taxonomy 2025](https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations-0) | 2025版、一次検索結果確認 | AI固有リスク分類の参考。詳細本文精査は次段階 |
| S21 | [MITRE ATT&CK ICS matrix](https://attack.mitre.org/matrices/ics/) | 2026-10-07一次検索結果確認 | ICS mapping候補。固定版ID対応表は今後作成 |
| S22 | [MITRE ATLAS](https://atlas.mitre.org/) | 一次検索結果確認 | AI脅威mapping候補。版固定とID対応は今後作成 |
| S23 | [FIDO specifications](https://fidoalliance.org/specifications/) | 一次検索結果確認 | origin-bound認証の参考。送金内容の承認と別扱い |
| S24 | [C2PA specification index](https://spec.c2pa.org/specifications/) | 一次検索結果確認 | 来歴検証の参考。正しさや送金権限の証明と別扱い |

## 確認できなかった情報

- `defcon.org` のDEF CON 34 village一覧、Tavus `/safety`、一部docs URLはこの取得経路で失敗。
  代わりに各主催者の本文とTavus AUPを使った。失敗を「安全対策なし」と解釈しない。
- DEF CON 34 main CTFの完全な問題・採点規則は本調査で確定していない。
  2025の明示的rulesを形式の参考にし、2026にも同一rulesだとは書かない。
- Black Hatは会場・年度・主催者で別競技。単一の「Black Hat CTF score」は定義しない。
- 本調査ではTavusが特定犯罪に使用されたこと、同意検証が破られたことを確認していない。
- ranking、金銭被害額、市場全体の悪用頻度、各防御策の阻止率は未測定。
