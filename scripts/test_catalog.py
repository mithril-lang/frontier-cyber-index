import json
import unittest
from pathlib import Path
from coverage import coverage
from grade_exercise import grade
ROOT=Path(__file__).resolve().parents[1]

class CatalogueTests(unittest.TestCase):
    def test_specs_are_original_and_references_resolve(self):
        sectors=json.loads((ROOT/'catalog/sectors.json').read_text())
        surfaces={s['id'] for s in json.loads((ROOT/'catalog/surfaces.json').read_text())}
        rows=json.loads((ROOT/'catalog/scenarios.json').read_text())+json.loads((ROOT/'catalog/cross-industry.json').read_text())
        self.assertEqual(len(rows),90)
        self.assertEqual(len({r['id'] for r in rows}),90)
        source_text=(ROOT/'reports/SOURCES.md').read_text()
        for r in rows:
            self.assertEqual(r['status'],'specification')
            self.assertEqual(r['grader_status'],'not-implemented')
            self.assertTrue(set(r['surfaces']) <= surfaces)
            for s in r['source_ids']: self.assertIn(f'| {s} |',source_text)
        for s in sectors:
            self.assertEqual({r['stage'] for r in rows if r['sector']==s['id']},{'A','B','C'})

    def test_offline_oracles_and_negative_controls(self):
        for p in (ROOT/'exercises').glob('*/reference-answer.json'):
            answer=json.loads(p.read_text())
            with self.subTest(exercise=p.parent.name):
                result=grade(p.parent.name,answer)
                self.assertTrue(result['complete'])
                self.assertEqual(result['total'],4)
                for action in ['allow','deny','unknown']:
                    wrong={'decisions':{k:action for k in answer['decisions']}}
                    self.assertFalse(grade(p.parent.name,wrong)['complete'])
                allow_all=grade(p.parent.name,{'decisions':{k:'allow' for k in answer['decisions']}})
                self.assertTrue(allow_all['unsafe_allow_events'])

    def test_invalid_submission_and_path_escape_fail_closed(self):
        for payload in [None,{},[],{'decisions':{}},{'decisions':{'F01':['allow']}},{'decisions':{},'score':100}]:
            with self.assertRaises(ValueError): grade('finance',payload)
        with self.assertRaises(ValueError): grade('../finance',{'decisions':{}})

    def test_coverage_does_not_claim_verification(self):
        c=coverage()
        self.assertEqual(c['sector_specs'],{'covered':24,'total':24})
        self.assertEqual(c['surface_specs'],{'covered':18,'total':18})
        self.assertEqual(c['offline_sector_coverage'],{'covered':8,'total':24})
        self.assertEqual(c['verified_frontier_runs'],0)
        self.assertLess(c['declared_sector_surface_cells'],c['possible_sector_surface_cells'])
