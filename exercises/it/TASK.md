# SaaS: tenant境界とOAuth scope

全て架空の合成証拠。L0教材。ネットワークも実人物の映像も不要。

## 問題

認証principal由来tenantとobject ownerが一致し、有効scope内なら許可。失効grantは拒否。

`evidence.json`の各eventを読んで、allow/deny/hold/unknown/escalate/deduplicateから一つを選び、
`answer-template.json`をコピーしたJSONのdecisionsに記入してください。観測されていない結果を推測しないでください。

## 提出と評価

```sh
python3 scripts/grade_exercise.py it /absolute/path/to/answer.json
```

これはrepo rootから実行します。根拠IDと理由、次に必要な確認先を別メモに書いてください。
自動採点はdecisionの一致だけを評価し、メモの正しさ・実運用での対応能力を認定しません。
`reference-answer.json`は学習用の公開正解。non-public benchmarkには使用できません。
