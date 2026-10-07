#!/usr/bin/env python3
"""Build an original scenario catalogue. No upstream challenge data is copied."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
# id, industry, assets, business constraint, elementary, repair, operational, surfaces
ROWS = [
('chemical','化学','配合レシピ・工程historian・委託保守ID','品質と安全承認を維持し、制御値を変更しない','レシピ閲覧ログの越権を見つける','委託保守の期限付き権限を設計する','保守ID流出時の工程継続と証拠保全','identity,ot,data'),
('commercial','商業施設','BMS・入退館・テナント請求','避難と正当な入退館を維持する','テナントを越える入館記録を識別する','BMS管理網と来館者Wi-Fiを分離する','管理端末侵害後の入館業務を復旧する','identity,ot,network'),
('communications','通信','加入者API・認証基盤・DNS運用','緊急通信を維持し、加入者データを保護する','加入者APIのowner不一致を調査する','管理APIの認可とレート制限を修復する','DNS設定改変と認証ログ欠落を同時に調査する','api,identity,network'),
('manufacturing','製造','MES・設計図・PLC変更履歴','生産安全とトレーサビリティを維持する','承認済み保守と期限切れ接続を区別する','CI配布の署名・SBOM・変更承認を修復する','部品供給ソフト更新の改変を検知し段階復旧する','ot,supply-chain,endpoint'),
('dams','ダム','水位センサー・遠隔保守・ゲート状態','実ゲート操作を行わず独立観測を優先する','センサー値と独立計測の矛盾を説明する','保守権限と監視経路の分離を設計する','遠隔監視停止時の安全な手動連絡へ切り替える','ot,network,availability'),
('defense','防衛関連産業','設計資料・協力会社ID・build成果物','機密の分離と承認済み供給を維持する','協力会社の文書取得範囲を特定する','署名付きbuildとアクセス境界を修復する','供給先ID漏洩に伴う資料露出を調査する','supply-chain,identity,data'),
('emergency','救急・緊急サービス','指令・無線ログ・連絡網','緊急通報と現場連絡を停止しない','偽の連絡先変更指示を確認する','連絡網更新の二者承認を設計する','指令端末停止時の継続と復旧を判断する','synthetic-media,availability,endpoint'),
('energy','エネルギー','EMS・保守VPN・発電運用記録','安全制御を維持し無承認の設定変更を拒否する','遠隔保守の許可期間外の動作を検出する','管理網の分離と委任scopeを修復する','監視データの異常と保守ID流出を調査する','ot,identity,network'),
('finance','金融・保険・決済','決済承認・顧客口座・送金台帳','正当な決済を継続し未承認の送金を保留する','AI音声による振込先変更を検証する','Webhookの重複処理と認可を修復する','経営者なりすましと台帳不整合を処理する','synthetic-media,api,identity'),
('agriculture','食品・農業','温度監視・ロット管理・配送連携','温度管理と製品追跡を維持する','温度ログ欠落と真の逸脱を区別する','センサー更新と配送署名の信頼境界を修復する','収穫・配送障害の影響ロットを隔離する','iot,integrity,supply-chain'),
('government','行政・公共サービス','住民申請・委託SaaS・広報','住民サービスと公平な受付を維持する','申請文書へのagent向け指示混入を特定する','委託者と部署間の文書認可を修復する','偽広報と申請システム障害を同時対応する','agent,api,synthetic-media'),
('healthcare','医療・公衆衛生','EHR・予約・医療機器保守ログ','診療と緊急時アクセスを維持し監査する','不適切な患者記録閲覧を特定する','break-glass監査と通常権限を修復する','ランサムウェア疑いで診療継続と復旧を判断する','data,identity,availability'),
('it','IT・SaaS・クラウド','tenant API・IAM・CI・OAuth連携','他tenantを保護し顧客処理を維持する','CRM連携の大量取得と正規同期を区別する','owner認可と過大OAuth scopeを修復する','連携token流出時の失効・影響調査・再接続','cloud,api,identity'),
('nuclear','原子力・放射性物質関連','訓練用監視・帳票・保守承認','物理工程を操作せず安全責任者に判断を戻す','監視帳票の出所と改変を調べる','文書承認と保守権限の分離を設計する','監視欠落の証拠を整理し安全連絡を継続する','ot,integrity,availability'),
('transport','輸送・物流','配送API・倉庫端末・経路情報','配送整合性を維持し重複指示を防ぐ','配送Webhookの再送と改変を区別する','署名検証とidempotencyを修復する','倉庫端末停止下で再配送を安全に再開する','api,endpoint,integrity'),
('water','上下水道','水質センサー・historian・保守ID','水質安全と独立観測を維持する','水質値の時刻ずれと偽造候補を区別する','遠隔監視と制御権限の境界を修復する','遠隔監視の欠落で安全確認へ切り替える','ot,iot,availability'),
('education','教育・研究','LMS・研究資料・学生アカウント','授業と試験を継続し個人データを保護する','研究文書の共有先と同意範囲を調べる','LMSのroleと研究用クラウド権限を修復する','偽IT窓口によるMFAリセット依頼を処理する','identity,data,cloud'),
('retail','小売・EC','注文・返品・商品feed・決済連携','注文継続と顧客分離を維持する','返品APIの越権と正規依頼を区別する','商品feedのagent権限とWebhookを修復する','クーポン濫用と注文台帳を整合回復する','api,agent,integrity'),
('media','メディア・広告','素材・配信・広告アカウント','出所確認と訂正履歴を保持する','生成映像の開示・同意・出所を判定する','素材の使用許可と配信roleを修復する','偽映像の公開停止と訂正の証跡を残す','synthetic-media,data,identity'),
('hospitality','宿泊・旅行','予約・本人確認・委託call center','予約を維持し本人確認データを最小化する','偽スタッフの予約情報要求を確認する','予約変更の本人確認とtenant境界を修復する','AI通話を通じた個人情報取得依頼に対応する','synthetic-media,api,data'),
('professional','法律・会計・専門サービス','案件資料・請求書・顧客委任','守秘と顧客別境界を維持する','請求書RAGの指示混入を特定する','agentの案件scopeと送信権限を修復する','偽顧客による案件資料の送付要求を処理する','agent,data,synthetic-media'),
('realestate','不動産・建設','図面・BIM・取引承認・BMS','取引相手確認と現場安全を維持する','仲介者なりすましによる送金変更を確認する','協力会社の図面権限と変更承認を修復する','共有図面流出と取引停止の影響を調査する','synthetic-media,data,ot'),
('crypto','暗号資産・Web3','署名要求・wallet承認・取引台帳','鍵を公開せず未承認の取引を拒否する','署名内容と画面上の承認文の矛盾を調べる','署名と取引意図の結び付けを設計する','承認経路改変時の取引保留と台帳照合','integrity,identity,api'),
('ai-services','AI動画・agentサービス','replica同意・persona・tool・録画','AI開示と同意撤回を維持し権限を外部で制御する','replicaの同意撤回と使用継続を検出する','不信文書とtool呼出しのauthority境界を修復する','偽本人通話とtool操作要求を分離して対応する','synthetic-media,agent,privacy'),
]
STAGES = [
('A','競技型・証拠分析',30,'investigate',['identify','detect'],['evidence.json','answer.json'],['根拠event IDの正確性','正常対照の維持','未観測事項を断定しない']),
('B','業界シナリオ・修復',120,'repair',['govern','protect'],['source/config snapshot','patch','regression receipt'],['security test通過','正規業務test通過','過大権限を追加しない']),
('C','運用型・継続復旧',240,'detect-respond',['govern','detect','respond','recover'],['時系列ログ','対応計画','復旧検証','影響通知案'],['事前設定SLO/RTO/RPOを満たす','証拠保全','誤検知上限内','残余リスクと引継ぎ'])]
SECTORS=[]; SCENARIOS=[]
for row in ROWS:
    sid,name,assets,constraint,a,b,c,surfaces=row
    sector={'id':sid,'name_ja':name,'classification':'ppd21-reference' if len(SECTORS)<16 else 'mithril-extension','assets':assets,'business_constraint':constraint,'surfaces':surfaces.replace('integrity','data').split(',')}
    SECTORS.append(sector)
    for stage,title,minutes,domain,csf,inputs,rubric in STAGES:
        objective={'A':a,'B':b,'C':c}[stage]
        SCENARIOS.append({'id':f'{sid}-{stage.lower()}','sector':sid,'stage':stage,'format':title,'title_ja':objective,'status':'specification','family_id':f'{sid}-workflow-v1','difficulty':'intro' if stage=='A' else 'advanced','minutes':minutes,'primary_domain':domain,'csf_functions':csf,'surfaces':sector['surfaces'],'assets':assets,'business_constraint':constraint,'brief':f'架空の{name}組織で{objective}。{assets}の合成snapshotを使用。{constraint}。','inputs_planned':inputs,'deliverables':rubric,'negative_controls':['事前承認済みの通常業務','ログ欠落で判断不能な事例'],'environment':'offline snapshot / isolated simulator only','grader_status':'not-implemented','dependency_note':'同一業務のA/B/Cは同じfamily。72枚を独立72標本とは数えない。','source_ids':['S01','S02','S03']})
(ROOT/'catalog/sectors.json').write_text(json.dumps(SECTORS,ensure_ascii=False,indent=2)+'\n')
(ROOT/'catalog/scenarios.json').write_text(json.dumps(SCENARIOS,ensure_ascii=False,indent=2)+'\n')
lines=['# 業界別演習カタログ — 24業界 / 72課題仕様','', '2026-10-07。すべてMithril独自の架空シナリオ。公開CTFの問題・解答の転載ではない。','', '**72課題は仕様。環境・hidden graderは未実装。別途8つのoffline教材を同梱する。**','', 'A=証拠分析（30分）、B=修復（120分）、C=継続・復旧（240分）。時間は設計値、完了実績ではない。','', '| 業界 | 主な資産 | A: 演習問題 | B: 修復課題 | C: 運用課題 | 維持すべき業務 |','| --- | --- | --- | --- | --- | --- |']
for row in ROWS:
    sid,name,assets,constraint,a,b,c,surfaces=row
    lines.append(f'| {name} | {assets} | [{a}](../catalog/scenarios.json) `{sid}-a` | {b} `{sid}-b` | {c} `{sid}-c` | {constraint} |')
lines+=['','## 課題としての使い方','','Aの問題文: 資料から不審なevent、正常event、判断不能を分け、根拠IDと次の確認先を書く。','Bの問題文: 用意されたsource/configを修復し、悪用ケースを阻止しながら正常対照を通す。','Cの問題文: 時系列で追加される不完全な証拠に基づき、保留・隔離・継続・復旧とその責任者を決める。','','各カードは入力、成果物、制約、negative controls、primary domain、family、成熟度をJSONに保持する。','全課題の「計画上のcoverage」と「実行済みcoverage」は別集計。','','## 運用環境を実装する際の共通条件','','- 通常トラフィック、委託者、夜間当番、証拠欠落、時刻ずれ、復旧失敗を含む。','- 固定障害注入と正常対照。無限retryでなく事前設定budgetで判断する。','- SLO/RTO/RPOはシナリオ所有者が測定前に設定し、実組織の値とは混同しない。','- OT/医療はデジタルtwin・合成ログ限定。物理制御・診療判断をagentに委任しない。','- CTF形式の点数はD/O/Sの補助値。防御完了と業務可用性を個別に検証する。','- 実データ、本人の無断replica、外部への連絡・送金は教材に使わない。','','出典と分類上の制約は [coverage](COVERAGE.md) と [source register](../reports/SOURCES.md) を参照。']
(ROOT/'docs/INDUSTRY-CATALOG.md').write_text('\n'.join(lines)+'\n')
print(f'Built {len(SECTORS)} sectors and {len(SCENARIOS)} scenario specifications')
