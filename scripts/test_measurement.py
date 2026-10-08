import unittest
from run_educational import require_budget, reservation, request_body, submission


class MeasurementTests(unittest.TestCase):
    def test_never_supplies_reference_answers(self):
        body = request_body('explicit/model', {'id': 'finance', 'policy': 'Synthetic', 'events': []}, 512)
        self.assertEqual(body['model'], 'explicit/model')
        self.assertNotIn('tools', body)
        self.assertFalse(body['provider']['allow_fallbacks'])
        self.assertNotIn('reference-answer', str(body))

    def test_refuses_duplicate_keys_and_executable_or_extra_output(self):
        for content in ['{"decisions":{},"decisions":{}}', '__import__("os")',
                        '{"decisions":{},"extra":true}', '{"decisions":{"F01":"allow"}}']:
            self.assertFalse(submission(content, 'finance')['valid'])

    def test_budget_rejects_nonfinite_negative_and_overrun(self):
        for spent, worst, cap in [(1.9, .2, 2), (0, 0, 3), (0, float('nan'), 2), (-1, .1, 2)]:
            with self.assertRaises(ValueError):
                require_budget(spent, worst, cap)
        require_budget(.1, .2, 2)

    def test_reserves_completion_and_framing_cost(self):
        body = request_body('explicit/model', {'id': 'finance'}, 512)
        worst = reservation(body, {'prompt': '.000002', 'completion': '.00001'})
        self.assertGreater(worst, .013)


if __name__ == '__main__':
    unittest.main()
