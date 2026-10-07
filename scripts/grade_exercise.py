#!/usr/bin/env python3
"""Offline educational scoring only. Does not execute answer content."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def grade(exercise, answer):
    valid={p.name for p in (ROOT/'exercises').iterdir() if (p/'evidence.json').exists()}
    if exercise not in valid:
        raise ValueError('Unknown exercise ID')
    expected=json.loads((ROOT/'exercises'/exercise/'reference-answer.json').read_text())['decisions']
    if not isinstance(answer,dict) or set(answer)!={'decisions'}:
        raise ValueError('Expected one decisions object')
    actual=answer['decisions']
    if not isinstance(actual,dict) or set(actual)!=set(expected) or any(not isinstance(v,str) for v in actual.values()):
        raise ValueError('Event IDs must match the fixture exactly, with string decisions')
    results={k:actual[k]==v for k,v in expected.items()}
    unsafe=[k for k,v in expected.items() if v in {'deny','hold','escalate','unknown','deduplicate'} and actual[k]=='allow']
    return {'exercise':exercise,'status':'educational-only','correct':sum(results.values()),'total':len(results),'unsafe_allow_events':unsafe,'complete':all(results.values()),'per_event':results}

if __name__=='__main__':
    try:
        if len(sys.argv)!=3:
            raise ValueError('Usage: python3 scripts/grade_exercise.py EXERCISE answer.json')
        answer=json.loads(Path(sys.argv[2]).read_text())
        result=grade(sys.argv[1],answer)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        sys.exit(0 if result['complete'] else 1)
    except (ValueError,OSError,TypeError) as e:
        print(json.dumps({'status':'invalid-submission','error':str(e)},ensure_ascii=False))
        sys.exit(2)
