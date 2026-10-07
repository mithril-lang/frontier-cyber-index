#!/usr/bin/env python3
"""Describe declared coverage; does not infer verified benchmark results."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def coverage():
    sectors=json.loads((ROOT/'catalog/sectors.json').read_text())
    surfaces=json.loads((ROOT/'catalog/surfaces.json').read_text())
    scenarios=json.loads((ROOT/'catalog/scenarios.json').read_text())
    cross=json.loads((ROOT/'catalog/cross-industry.json').read_text())
    packs=[json.loads(p.read_text()) for p in sorted((ROOT/'exercises').glob('*/evidence.json'))]
    sid={s['id'] for s in sectors}; tid={s['id'] for s in surfaces}
    declared={s['sector'] for s in scenarios}; technical={t for s in scenarios+cross for t in s['surfaces']}
    cells={(s['sector'],t) for s in scenarios for t in s['surfaces'] if t in tid}
    return {'as_of':'2026-10-07','sector_specs':{'covered':len(sid & declared),'total':len(sid)},'surface_specs':{'covered':len(tid & technical),'total':len(tid)},'industry_scenario_specs':len(scenarios),'cross_industry_specs':len(cross),'declared_sector_surface_cells':len(cells),'possible_sector_surface_cells':len(sid)*len(tid),'offline_exercises':len(packs),'offline_decisions':sum(len(p['events']) for p in packs),'offline_sector_coverage':{'covered':len(sid & {p['id'] for p in packs}),'total':len(sid)},'offline_surface_coverage':{'covered':len(tid & {t for p in packs for t in p['surfaces']}),'total':len(tid)},'verified_frontier_runs':0,'missing_offline_sectors':sorted(sid-{p['id'] for p in packs}),'missing_offline_surfaces':sorted(tid-{t for p in packs for t in p['surfaces']}),'qualification':'design-and-educational-fixtures-only'}

if __name__=='__main__':
    print(json.dumps(coverage(),ensure_ascii=False,indent=2))
