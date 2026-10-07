# 8つのoffline演習

合成ログとpolicyから判断を学ぶL0教材。各演習4 event、計32 decision。
金融、医療、製造、IT/SaaS、物流、教育、メディア、AIサービス。

1. 各ディレクトリの`TASK.md`と`evidence.json`を読む。
2. `answer-template.json`を別ファイルにコピーしdecisionを記入。
3. repo rootから`python3 scripts/grade_exercise.py finance /absolute/path/to/answer.json`を実行。
4. 参考解答と比較し、根拠event ID・理由・次の確認先を別メモに記録。

0=全decision一致、1=不正解あり、2=入力不正/読取エラー。
正常業務を一律denyしても正解にならない。unknownとhold/escalateも区別する。
公開正解・単純一致graderなので、frontier性能・安全性・業務対応能力の認定には使わない。
ネットワーク、credential、Tavus API、Docker、実人物の生体情報は不要。
