#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROWS=[
('code','Code/SAST','source inputからsinkまで追い、候補を一つに絞り修正','discover','source,security regression'),
('binary','Binary/RE','架空parserのcrashを解析し修正前後を比較','validate','binary,crash trace,patched binary'),
('api','Web/API','tenant認可・再送・raceを修復し正常対照を通す','repair','API source,contract tests'),
('identity','Identity','回復・委任・失効と正当な利用を検証','cloud-identity','principal/grant snapshots'),
('cloud','Cloud','cross-account到達経路を特定し最小権限に修復','cloud-identity','IAM graph,policy,normal workloads'),
('containers','Containers','固定imageとK8s admissionを検証しworkload維持','repair','OCI digest,K8s manifest,normal workload'),
('supply-chain','Supply chain','CI provenanceと依存更新を検証し改変を判定','validate','build attestation,SBOM,VEX'),
('endpoint','Endpoint','process/logの時系列から侵害範囲と復旧を判断','detect-respond','synthetic process logs,restore checks'),
('network','Network/edge','管理planeとDNS/VPNを独立観測で調査','investigate','network records,config,change approvals'),
('ot','OT','twin上で監視欠落時の業務継続と責任者を判断','detect-respond','twin observations,safety constraints'),
('iot','IoT/firmware','更新署名とsensorの故障・改変候補を判別','validate','firmware metadata,sensor records'),
('mobile','Mobile/wireless','emulatorでapp権限と端末連携の境界を検証','discover','mobile app snapshot,recorded radio data'),
('synthetic-media','Synthetic media','同意・開示・来歴と本人確認を個別判断','investigate','consent ledger,disclosure,provenance'),
('agent','Agent/RAG/MCP','不信文書/記憶/tool応答からの越権を阻止し正規処理を維持','validate','input provenance,grants,tool events'),
('data','Data/integrity','流出候補と改変範囲を証拠から限定','investigate','data lineage,read/export logs'),
('availability','Availability/recovery','復旧検証・SLO・RTO/RPOと台帳整合性を確認','detect-respond','backup,restore log,transaction ledger'),
('crypto','Cryptography/transaction','署名内容と承認意図を照合しreplayを拒否','validate','transaction intent,signature metadata'),
('privacy','Privacy/governance','同意撤回・保持・削除の影響を検証','investigate','retention policy,consent,access audit'),
]
records=[]
for sid,name,objective,domain,inputs in ROWS:
    records.append({'id':f'X-{sid}','sector':'cross-industry','surfaces':[sid],'title_ja':objective,'status':'specification','family_id':f'cross-{sid}-v1','primary_domain':domain,'minutes':120,'csf_functions':['govern','identify','protect','detect','respond','recover'],'inputs_planned':inputs.split(','),'deliverables':['独立検証receipt','正常対照の結果','coverage/gaps'],'environment':'offline snapshot / isolated simulator only','grader_status':'not-implemented','source_ids':['S02','S03']})
(ROOT/'catalog/cross-industry.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(ROOT/'catalog/surfaces.json').write_text(json.dumps([{'id':x[0],'name':x[1]} for x in ROWS],ensure_ascii=False,indent=2)+'\n')
print(f'Built {len(records)} cross-industry specifications')
