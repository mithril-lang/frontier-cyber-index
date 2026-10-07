# AI動画・agent技術の悪用リスク調査 — Tavusを含む

調査基準日: 2026-10-07（JST）。対象: 公開一次資料から確認できる機能・対策・観測事例と、
Mithrilによる防御側の脅威分析。侵入実行、サービスの安全対策の突破、人物の無断複製は実施していない。
出典の確認状態と日付は[台帳](SOURCES.md)に記録する。

## 要旨

リアルタイムの顔・声・対話と、文書検索・tool操作・SaaS連携が組み合わさると、
「誰に見えるか」「誰が認証されたか」「何を承認したか」の境界が重要になる。
自然な対話の見た目だけで送金、資料送付、本人確認の例外処理を認める構成は危険になり得る。
これはMithrilの脅威分析であり、特定提供者の不正や脆弱性の発見ではない。

## 1. 確認した事実と、推論を分ける

| 区分 | 記載できること | 限界 |
| --- | --- | --- |
| 提供者の機能説明 | TavusはPhoenix-4.5（描画）、Raven-1（音声/映像知覚）、Sparrow-2（対話の流れ）を説明 [S11](SOURCES.md) | 性能・感情推定の精度は本調査で実測していない |
| 構成例 | Tavus Engineeringのintake資料にpersonaのLLM toolsとtool_call eventがある [S12](SOURCES.md) | 全用途に金融/業務操作が既定であるとは言わない |
| 提供者の利用要件 | Tavus AUPは本人の明示的同意、AI開示、同意撤回の尊重等を要求 [S13](SOURCES.md) | 技術的な阻止率や検証の突破可能性は未確認 |
| 一般的悪用の警告 | FBI/IC3はAI音声・動画を使うなりすまし/詐欺を警告 [S14–15](SOURCES.md) | これらの事例にTavusが使われたという帰属はない |
| 提供者の観測 | Anthropicの2026年9月reportはcyber operationsと詐欺等の事例を掲載 [S19](SOURCES.md) | その提供者が見た偏った母集団。市場全体の率や一般性能ではない |
| 防御側の想定 | 会話の本人らしさが業務権限に誤変換されると被害が生じ得る | 以下はMithrilの分析。観測済み事件と混ぜない |

## 2. 最近の更新をどう評価に取り込むか

- **2026年9月**: OWASPはLLM Top10新版とAgent Control Standard等を案内。
  riskの分類とruntime側の制御を併せて評価する参考になる。[発表 S17](SOURCES.md)
- **2026-09-10公開、2025-12〜2026-08の活動**: Anthropicはサービス悪用の事例を報告。
  autonomous workflowやdeceptive personaのような、複数段階の活動を扱う。
  事例の存在から万能な自律攻撃能力や被害件数を推定しない。[report S19](SOURCES.md)
- **2026年8月イベント案内**: DEF CON 34 Cloud VillageはIAM、DevOps、cloud defense等を扱う。
  abstractの主張を独立した実証とみなさず、評価課題の候補として利用。[S07](SOURCES.md)
- **2026年9月planning note**: NISTのOT guideはr4初期draftへの参照を追加。
  r3 finalとdraftを区別し、安全制約をtask manifestに残す。[S03–04](SOURCES.md)

「最近」は公開日・版と確認日に結びつける。Tavusの機能名は調査日の公開説明であり、
直近にすべて新規releaseされたという意味ではない。新機能のrelease日は未確定。

## 3. 悪用され得る技術と防御への落とし込み

次表は**Mithrilの脅威分析**。攻撃手順、回避payload、実人物のclone素材は含めない。
優先度は被害の重大性・権限境界・業務普及から置く設計値で、実測された発生率ではない。

| 技術 | 成立を許す弱い境界 | 想定される被害 | 優先度 | 防御・測定する課題 |
| --- | --- | --- | --- | --- |
| Real-time avatar/video | 顔の一致を取引承認と同一視 | BEC、偽面接、偽窓口、予約情報取得 | P0 | 登録済み経路で本人確認、取引内容に結びつく承認。finance-a/media-a |
| Voice cloning/低遅延音声 | 音声を認証の唯一要素にする | 偽上司・家族・保守担当、MFA回復濫用 | P0 | 独立callback、別権限者の確認、正常call対照。education-c |
| Persona/多言語会話 | 信頼と権限付与を分離しない | 偽相談員、投資勧誘、回収詐欺 | P0 | 人間への確認、AI開示、金銭/秘密へのauthority分離。hospitality-c |
| Perception/感情推定 | 視線・感情推定を本人性/判断能力と扱う | 推測による不当な判断、過剰データ保持 | P1 | 推定不確実性、利用制限、保持最小化。ai-services-a |
| Agentic code/tool | 不信inputがtool permissionになる | 越権操作、資料流出、不適切な修復 | P0 | broker側のprincipal/目的/scope検証、正常tool維持。X-agent |
| RAG/文書/永続memory | 文書と上位指示の区別が失われる | 判断誘導、次sessionへの汚染 | P0 | input provenance、memory隔離、正常引用対照。professional-a |
| MCP/plugin/skills | 説明文や導入が権限委任になる | token/資料露出、supply chain汚染 | P0 | 固定identityと権限grant、tool差分、失効試験。X-supply-chain |
| Browser/desktop automation | 表示上の指示を認証済み操作に変える | 送信・設定変更・account recovery濫用 | P0 | originと操作authority、確認済み宛先、追跡receipt。X-endpoint |
| SaaS/OAuth integrations | 一度の委任で過大なscopeが永続化 | tenant横断取得、大量export、二次連鎖 | P0 | 有効principalとscope、失効/read-back、正常sync。it-c |
| Image/document generation | 文書の外観を出所と扱う | 偽請求書・本人資料・広報 | P1 | 独立原本確認、署名/来歴の検証範囲。government-c |
| AI gateway/model routing | model keyと業務authorityを同居させる | 秘密露出、不正推論費、model差替え | P0 | credential broker、model snapshot、budget/lease。X-cloud |
| CI/OSS/model artefacts | 可変依存・署名だけで信頼を決める | 改変成果物の配布、grader汚染 | P0 | digest、再現build、独立grader、正常update。manufacturing-b |
| Edge/VPN/identity plane | 管理経路の集中と観測への盲信 | 広範な権限・ログの信頼性喪失 | P0 | 独立telemetry、権限分離、復旧検証。X-network |
| IoT/OT/robotics | sensor入力と制御authorityの直結 | 安全影響、工程停止、誤った復旧 | P0 | twin、独立計測、人間安全責任者。water-c/dams-c |
| Media provenance | 署名有無を真偽/同意/本人性と同一視 | 誤認、出所の過信、不当な除外 | P1 | 来歴・同意・内容確認を個別採点。X-synthetic-media |
| Crypto/transaction signing | 表示と実署名内容の不一致 | 未承認の取引、誤送付 | P0 | intent-bound approval、simulation、replay検証。crypto-a |

## 4. Tavus型のサービスを検証する具体的な境界

Tavusの対策の突破を仮定せず、導入側の責任を模擬環境で評価する。

1. **作成**: replica対象者の同意・用途・期限を記録する。公開映像があることは同意ではない。
2. **対話**: AIであると開示し、本人確認が必要な場面は独立した認証に戻す。
3. **操作**: 会話personaに何ができるかをpromptだけで決めず、外部brokerで権限検証。
4. **録画/知覚**: 音声・映像・推定属性の保持範囲、閲覧者、削除/撤回を別々に扱う。
5. **例外**: 認証回復・緊急依頼・送金変更は既存の確認済み業務経路を使う。
6. **終了**: 同意撤回、tool grant失効、録画保持と後続sessionの状態をread-backする。

[S13: 提供者AUP](https://www.tavus.io/acceptable-use-policy)を参考にしたMithrilの評価提案。
機能や設定がこのすべてを提供することを主張しない。

## 5. 業界ごとの優先順位

金融は送金承認、医療は診療継続と患者データ、製造/energy/waterは安全と監視、
物流/ECはtransaction整合性、教育はaccount recovery、メディアは素材同意と来歴、
行政は住民サービスと公的発信、専門サービスは守秘と委任を初期課題にする。
これは架空シナリオの設計判断であり、各業界の被害順位の統計ではない。
24業界の問題文と制約は[カタログ](../docs/INDUSTRY-CATALOG.md)にまとめる。

## 6. 対策の限界も採点する

- deepfake detectorの当たり外れだけで本人性を決めない。未知の生成方式、圧縮、noiseも別stratum。
- Content Credentialsは来歴の手掛かり。存在しても発言内容や取引authorityを保証せず、
  ないだけで偽物と断定しない。C2PA仕様は[参考 S24](SOURCES.md)、詳細精査は次段階。
- passkeyでloginを保護しても、回復窓口・既存session・取引内容承認を別途検証する。
  origin-bound認証は[FIDO参考 S23](SOURCES.md)、導入案はMithrilの分析。
- すべてを拒否するsystemが高得点にならないよう、正常task完了率を必ず併記する。
- 文書や台帳の存在を実装済み対策とみなさない。阻止eventと通過eventを観測する。

## 7. 今回の成果と残る検証

成果: 24業界/72業界課題仕様、18技術領域の横断仕様、8つの合成証拠教材、出典台帳。
未完: 独立hidden grader、実コード修復環境、長時間range、全業界の専門家レビュー、モデル実測。
公開教材の正解は学習用に公開するため、non-public holdoutとは独立させる。
実際の悪用率・Tavus対策の阻止率・MFCI model scoreをこの調査から生成しない。
