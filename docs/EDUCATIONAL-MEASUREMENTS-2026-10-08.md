# 初回の公開教材測定 — 2026-10-08

Mithril Analysis の測定・証跡経路を確認するため、公開済みの8教材を
2モデル × 各3回で実際に呼び出した。48応答、192 decision を記録した。
これは公開解答のある教材での観測であり、MFCI-D/O/S、非公開 holdout、
CTF 実行、脆弱性修正能力、実運用対応能力の測定ではない。

| 要求・応答モデル ID | 呼出回数 | decision 一致 | 危険側 allow | 観測 API 費用 (USD) |
| --- | ---: | ---: | ---: | ---: |
| openai/gpt-6.1-sol | 24 | 87 / 96 | 0 | 0.02624 |
| anthropic/claude-sonnet-5.5 | 24 | 84 / 96 | 0 | 0.03240 |

合計費用は provider usage の記録を加算している。決定の一致率を
モデルの総合順位に使わない。3回の反復は同じ32判断の繰り返しであり、
96個の独立な未知課題ではない。dangerous allow は、この教材の公開解答が
deny/hold/escalate/unknown/deduplicate なのに allow と答えた件数に限る。
その他の不一致を無害と認定する指標ではない。

## 記録と再現

- 生の合成入力、応答、採点結果、時刻、経過秒、usage、generation ID:
  [JSON receipt](../results/educational-2026-10-08.json)
- 凍結済み harness と教材 commit: `d1aaa7a`（完全 SHA は receipt）。
- harness、入力、応答、grader、公開解答を SHA-256 で記録。
- OpenRouter の chat completions を使用。tools・モデル用ネットワークなし。
- 各呼出は新しい会話。公開解答・grader・過去の応答はモデルに送っていない。
- reasoning effort `low`、出力上限1024、provider fallbackなし。
- 推定費用を各呼出前に予約し、全体上限2ドル。未知結果は再試行しない。
- モデル ID は要求と応答で一致したが、immutable weights snapshot は確認できない。

公開正解・単純一致 grader の制約は解消されていない。入力に正解を
渡さないことは、学習汚染の不存在や採点の独立性を証明しない。
比較対象が2モデル、各3回の小規模観測なので、有意差・順位を主張しない。

## 正式な frontier 測定に残ること

6 defensive domain の task family を実装し、公開教材と重ならない
非公開 holdout を凍結する。agent tools と隔離環境、独立 grader、
model snapshot、停止・費用ルールを事前登録し、paired Mithril comparison
と family 単位の推定を実行する。独立レビューと task validity の確認前に
この教育測定を正式 leaderboard に算入しない。

API の契約は [OpenRouter の公式仕様](https://openrouter.ai/docs/api/api-reference/chat/send-chat-completion-request)
を参照。プロバイダーの仕様が成立しても、評価設計の妥当性を意味しない。
