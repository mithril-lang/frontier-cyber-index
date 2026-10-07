# Coverageを最初に定義する

更新: 2026-10-07。ここでのcoverageは**計画・教材・検証**を別々に表す。
分類を揃えることは、全攻撃を防げること・全業務を評価済みという意味ではない。

## 1. 業界の母集団

NISTが記載するPPD-21由来の米国重要インフラ16分類を基礎にし、Mithrilの8分類を追加。
[一次資料 S01](../reports/SOURCES.md)を参照。追加分類は教育、EC、メディア、宿泊、専門サービス、
不動産、暗号資産、AIサービス。商業施設とEC/宿泊などは重なるため、独立母集団とは数えない。
これはMithrilの初期taxonomyであり、日本の重要インフラ制度の完全対応表ではない。
SMB/大企業/公共組織、委託者、地域、使用言語は各業界を横断する追加stratumとする。

[24業界・72課題仕様](INDUSTRY-CATALOG.md)と機械可読な[業界JSON](../catalog/sectors.json)を作成。
業界別の調達・法令・現場安全の精査は専門家レビューとして残す。

## 2. 技術面の18領域

| 領域 | 課題で測ること | 提出物・正常対照 |
| --- | --- | --- |
| Code/SAST | inputからsink、認可漏れ、修正 | source位置・patch・security/機能tests |
| Binary/RE | crash原因、境界、修正の再現性 | 架空binaryの解析・修正前後の挙動 |
| Web/API | object認可、session、Webhook、race | tenant別tests・署名/再送/重複test |
| Identity | IAM、OAuth、MFA回復、委任 | principalとscope・正規利用の維持 |
| Cloud | reachability、cross-account、構成 | graph・最小権限config・正負case |
| Containers | image、K8s、runtime分離 | digest・policy・workload回帰 |
| Supply chain | CI、署名、依存、SBOM/VEX | provenance・固定source・update判断 |
| Endpoint | process/log、侵害範囲、復旧 | time line・正常admin作業の区別 |
| Network/edge | DNS、VPN、管理plane、暗号設定 | 独立観測・運用変更の承認 |
| OT | historian、保守、zone、安全責任 | simulatorの安全条件と監視継続 |
| IoT/firmware | 更新署名、sensor、device ID | 正規更新・sensor故障の対照 |
| Mobile/wireless | app権限、QR、端末連携、無線境界 | emulator/記録データ・許可端末 |
| Synthetic media | voice/video、replica同意、来歴 | consent/撤回/開示・独立本人確認 |
| Agent/RAG/MCP | 不信input、tool、memory、委任 | policy decision・正常tool完了 |
| Data/integrity | exfil候補、改変、tenant分離 | data lineage・未観測の明記 |
| Availability/recovery | outage、backup、SLO/RTO/RPO | restore test・一貫性・継続計画 |
| Cryptography/transaction | key用途、署名意図、replay | 正規取引・改変/再送拒否 |
| Privacy/governance | 最小化、保持、削除、アクセス | retentionと監査・同意撤回 |

業界で不足する面はcross-industry仕様で補う。暗号の暗記問題だけでは鍵運用能力を認定しない。
物理安全を伴う無線/OTはemulatorと記録データ限定で、実電波送信や制御は含めない。

## 3. 業務ライフサイクルと評価軸

NIST CSF 2.0の6 Functionsは[一次資料 S02](../reports/SOURCES.md)に従う参照軸。
MFCIのD/O/S、業界、技術、CSF、難度、task形式、証拠、成熟度を独立フィールドにする。
Governはowner・変更承認・同意、Identifyはinventory、Protectは権限/patch、
Detectはログと正常対照、Respondは保留/隔離、Recoverは検証済み復旧として出題する。
規格へのmappingは認証や法令適合の宣言ではない。

## 4. CTFから運用へ変換する原則

| 参考 | 確認した形式 | Mithrilで追加する条件 |
| --- | --- | --- |
| DEF CON 33 main CTF | attack/defend・patch・サービス維持 | 個別の安全権限、修正の機能回帰、対応証跡 |
| DEF CON 34 Cloud Village | cloud/IAM/DevOpsとCTF | owner/tenant、委託token、継続と復旧 |
| DEF CON 34 OWASP CTF | village競技 | Web/AI問題の正常業務対照 |
| Black Hat training exams | CTF/実技/scenario/project評価 | 業界の業務制約とend-to-end成果物 |
| Black Hat USA 2026 summits | 医療・AI・金融等の業界テーマ | 同じ技術でも異なる被害と停止条件 |

出典[S06–S10](../reports/SOURCES.md)。公式の問題を複製したり、イベントの支持を示すものではない。
競技のflag、patch適用、サービス生存、被害抑止、復旧完了を別々に記録する。
main CTF/village/ベンダーCTFを一つのbenchmarkとして合算しない。

## 5. 分母を隠さない

- 計画coverage = 有効な仕様がある領域数 / 事前登録taxonomyの領域数。
- 教材coverage = fixtureと採点器がある領域数 / 同じ母集団。
- 検証coverage = 独立grader・正負control・反復receiptが揃う領域数 / 同じ母集団。
- 業界×技術の交差cellも数える。24業界と18領域の両端が揃っても432cellすべてを網羅とは言わない。
- 重複するfamily・同じblueprintの業界名替えを独立標本として数えない。
- 8つのoffline教材の正解確認は教材の動作確認。frontier評価・本番能力の結果には使わない。

`python3 scripts/coverage.py` が台帳に基づく件数とgapを出す。
最初に閉じるべきgapは、binary/mobile/containerの実行環境、独立hidden grader、
業界専門家のレビュー、長時間E2E、モデル実測、人間基準、規格IDの版固定。

## 6. 難度とリリース

L0=offline証拠読み、L1=単独の修復/検知、L2=複数システム連携、L3=継続/復旧、
L4=人間専門家の時間を測定した非公開holdout。難度は名称から推測せずpilotで較正。
今回の公開教材はL0。A/B/CカードはL1–L3を実装するための仕様。
既存DESIGN.mdの120 family pilotとは別の公開教材cohortで、数を足さない。
本番対象の検証には別の明示的scopeと実環境receiptが必要。
