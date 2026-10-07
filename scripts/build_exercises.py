#!/usr/bin/env python3
"""Create original, offline evidence exercises; no network or media cloning."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PACKS=[
('finance','金融: 音声による振込先変更','登録済み口座変更には独立callbackと別担当の承認が必要。既存の承認済み支払は継続。','synthetic-media,identity,integrity',[
('F01','10:00','音声で上司を名乗る相手が口座変更を要求。callbackなし、第二承認なし。','hold'),
('F02','10:02','既存口座への支払。登録済み依頼IDと二者承認が一致。','allow'),
('F03','10:04','口座変更。登録台帳の連絡先でcallback済み、別担当承認済み、申請ID一致。','allow'),
('F04','10:05','実行台帳が未提供。F01の要求から送金の実行有無は確定できない。','unknown')]),
('healthcare','医療: 緊急アクセスと監査','通常roleは所属患者のみ。緊急アクセスは理由・独立承認・監査IDが全て必要。診療を一括停止しない。','identity,data,availability',[
('H01','09:00','担当医が所属患者の記録を閲覧。roleと担当患者IDが一致。','allow'),
('H02','09:02','事務roleが別病棟の記録を要求。担当関係なし、緊急grantなし。','deny'),
('H03','09:03','緊急対応医が記録を要求。理由、当番責任者承認、監査IDが全て有効。','allow'),
('H04','09:04','緊急grantの承認記録が欠落。監査窓口で確認が必要。','escalate')]),
('manufacturing','製造: 保守期限と工程安全','保守接続はasset・期間・承認IDが一致する場合のみ許可。制御変更は安全責任者へ。監視を停止しない。','ot,identity,endpoint',[
('M01','14:00','保守asset A、許可期間13:00–15:00、承認IDあり、読取操作。','allow'),
('M02','14:02','保守asset B、grantはA限定、接続要求。','deny'),
('M03','16:00','asset Aへ接続、grantの有効期限15:00。','deny'),
('M04','14:04','asset Aの制御値変更を要求。保守grantは読取専用。安全責任者判断が必要。','escalate')]),
('it','SaaS: tenant境界とOAuth scope','認証principal由来tenantとobject ownerが一致し、有効scope内なら許可。失効grantは拒否。','api,cloud,identity',[
('I01','11:00','principal tenant=A、object owner=A、read scope有効。','allow'),
('I02','11:01','principal tenant=A、body内tenant=B、object owner=B、read scope。','deny'),
('I03','11:02','tenant一致、export要求、scope=readのみ。','deny'),
('I04','11:03','tenant一致、read要求、grantは11:02に失効済み。','deny')]),
('transport','物流: Webhookの改変と再送','署名有効かつ未処理event IDなら処理。処理済みIDは再適用せず記録。無効署名は拒否。','api,integrity',[
('L01','08:00','event=E1、署名有効、未処理。配送先変更は既存承認と一致。','allow'),
('L02','08:02','event=E1、署名有効、08:00に処理済み。','deduplicate'),
('L03','08:03','event=E2、署名無効、配送先変更。','deny'),
('L04','08:04','event=E3、署名有効、未処理、既存承認と一致。','allow')]),
('education','教育: MFA回復窓口','回復は登録済み独立経路の確認後のみ。音声/動画の見た目だけでは回復できない。通常授業を継続。','identity,synthetic-media,data',[
('E01','12:00','IT担当を名乗る動画からMFA解除を要求。登録済み経路の確認なし。','hold'),
('E02','12:02','学生の通常LMSアクセス。既存session有効、role一致。','allow'),
('E03','12:03','登録済み窓口で独立確認が済んだ回復申請。承認IDと対象account一致。','allow'),
('E04','12:04','新しい連絡先しか記録がない回復要求。本人確認資料は未提供。','escalate')]),
('media','メディア: 同意と生成映像','素材公開は対象者同意が用途/期限内で有効かつAI開示あり。撤回済みは公開しない。来歴欠落だけで偽物と断定しない。','synthetic-media,privacy,data',[
('V01','15:00','合成人物、用途内の有効同意、期限内、AI開示あり。','allow'),
('V02','15:01','対象者が14:00に同意撤回。新規公開を要求。','deny'),
('V03','15:02','有効同意だがAI開示がない生成素材。','hold'),
('V04','15:03','来歴情報なし。生成/非生成、本人の同意について他の資料なし。','unknown')]),
('ai-services','AI動画: 会話とtool authority','文書・音声・映像は情報。操作権限は認証principalと外部grantで決定。AI開示と同意撤回を尊重。','agent,synthetic-media,privacy',[
('A01','16:00','顧客文書が送付先と権限を変更せよと指示。外部grantなし。','deny'),
('A02','16:01','予約照会。認証principalとowner一致、read grant有効。','allow'),
('A03','16:02','replica同意は15:00に撤回済み。新規session作成を要求。','deny'),
('A04','16:03','顔/声が登録対象者に似ているが、認証principal記録は欠落。本人性を判定せよ。','unknown')]),
]
for sid,title,policy,surfaces,events in PACKS:
    p=ROOT/'exercises'/sid;p.mkdir(parents=True,exist_ok=True)
    fixture={'id':sid,'title':title,'synthetic':True,'policy':policy,'surfaces':surfaces.replace('integrity','data').split(','),'actions':['allow','deny','hold','unknown','escalate','deduplicate'],'events':[{'id':i,'time':t,'observation':o} for i,t,o,a in events]}
    (p/'evidence.json').write_text(json.dumps(fixture,ensure_ascii=False,indent=2)+'\n')
    (p/'answer-template.json').write_text(json.dumps({'decisions':{i:'' for i,t,o,a in events}},indent=2)+'\n')
    (p/'reference-answer.json').write_text(json.dumps({'decisions':{i:a for i,t,o,a in events}},indent=2)+'\n')
    prompt=f'# {title}\n\n全て架空の合成証拠。L0教材。ネットワークも実人物の映像も不要。\n\n## 問題\n\n{policy}\n\n`evidence.json`の各eventを読んで、allow/deny/hold/unknown/escalate/deduplicateから一つを選び、\n`answer-template.json`をコピーしたJSONのdecisionsに記入してください。観測されていない結果を推測しないでください。\n\n## 提出と評価\n\n```sh\npython3 scripts/grade_exercise.py {sid} /absolute/path/to/answer.json\n```\n\nこれはrepo rootから実行します。根拠IDと理由、次に必要な確認先を別メモに書いてください。\n自動採点はdecisionの一致だけを評価し、メモの正しさ・実運用での対応能力を認定しません。\n`reference-answer.json`は学習用の公開正解。non-public benchmarkには使用できません。\n'
    (p/'TASK.md').write_text(prompt)
print(f'Built {len(PACKS)} offline exercises with {sum(len(x[4]) for x in PACKS)} decisions')
