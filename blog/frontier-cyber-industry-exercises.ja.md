# サイバー演習を業界の仕事につなげる：Mithrilのcoverage設計

2026-10-07。MFCI v0.1の設計と公開教材の紹介。モデルの実測結果はまだありません。

サイバー演習で問題を解けたとき、その結果を業務にどう結び付ければよいでしょうか。
金融では正当な送金を続けながら未承認の変更を止める必要があります。医療では患者データを
守りながら診療を続け、製造では安全と監視を維持する必要があります。Mithrilは、こうした
違いを最初から評価対象に入れるため、業界・技術・業務工程ごとのcoverageを整理しました。

## 競技から学び、業務条件を加える

DEF CON 33の公式規則は、攻撃と防御、patchによるサービス維持を組み合わせています。
2026年のCloud VillageはcloudやIAM等を扱い、Black Hatのtraining評価にはCTFに加えて
実技・scenario・project形式があります。Mithrilはこれらの形式を参考にします。
大会ごとの採点結果を混ぜたり、公式問題を転載するものではありません。
[DEF CON 33 rules](https://nautilus.institute/files/rules-2025-100.pdf)、
[Cloud Village 2026](https://www.cloud-village.org/dc34)、
[Black Hat training exams](https://blackhat.com/html/certificates.html)。

演習は三段階です。Aは証拠を読んで異常・正常・判断不能を区別する問題。
Bはsourceや設定を修復し、悪用ケースを止めながら正常業務を通す課題。
Cは不完全なログが順次届く状況で、保留・隔離・継続・復旧を判断する課題です。
復旧は再起動だけで終わらず、台帳や権限が整合しているかも検証します。

## 最初にcoverageの分母を決める

初期分類は24業界、18技術領域です。業界は[NISTの米国重要インフラ16分類](https://csrc.nist.gov/glossary/term/critical_infrastructure_sectors)
を参考に、教育・EC・メディア・宿泊・専門サービス・不動産・暗号資産・AIサービスを追加。
重なる業界もあり、世界共通の分類や日本の制度の完全対応表ではありません。
技術面にはWeb/API、IAM、cloud、supply chain、OT、mobile、音声・動画、agent/RAG/MCP等を含めます。

公開したのは72の業界課題仕様、18の横断課題仕様と8つのoffline教材です。
仕様が揃った範囲、教材が動く範囲、独立した採点器でモデルを実測した範囲を分けます。
24業界と18領域の名前が揃っても、432の組み合わせを全て検証済みとは表示しません。
[coverage台帳](https://github.com/mithril-lang/frontier-cyber-index/blob/main/catalog/coverage.json)
で不足も確認できます。

## 実運用に近づけるための採点条件

| 業界 | 初期課題 | 守り続けること |
| --- | --- | --- |
| 金融 | AI音声による振込先変更 | 正規支払、独立確認、取引内容の承認 |
| 医療 | 緊急アクセスと監査 | 診療継続、患者分離、緊急grantの記録 |
| 製造 | 期限切れの委託保守 | 工程安全、許可asset、監視継続 |
| IT/SaaS | tenant認可とOAuth | 顧客分離、最小scope、正常同期 |
| 物流 | Webhook再送と改変 | 一度だけの適用、配送台帳の整合 |
| メディア | 生成映像の同意・開示 | 同意撤回、来歴確認、訂正履歴 |

これはMithrilの架空課題の設計で、実際の事故や現場の再現ではありません。
全て拒否するsystemも高得点にしません。正常業務の成功率、誤検知、証拠欠落、費用、時間を
併記します。MFCIの防御能力D、攻撃能力O、安全性Sは別々に測定します。
Mithrilの寄与は、同じモデル・同じ課題をMithrilあり/なしで比較する計画です。

## 教材を使い、残るgapを確認する

[GitHub repository](https://github.com/mithril-lang/frontier-cyber-index)には合成証拠と回答template、
採点器、公開参考解答があります。ネットワークや実人物の音声・動画は不要です。
8教材はL0の判断練習で、実コード修復や長時間rangeの代わりにはなりません。
採点器のpositive/negative controlを確認しても、frontier modelの能力を実測したことにはなりません。

次に必要なのは、業界専門家によるレビュー、実行環境、独立hidden grader、
非公開holdout、人間の基準測定です。[全業界カタログ](https://github.com/mithril-lang/frontier-cyber-index/blob/main/docs/INDUSTRY-CATALOG.md)
から、自分の業界の維持すべき業務と欠けている条件を確認してください。
最新技術については[AI動画・agentの調査レポート](https://github.com/mithril-lang/frontier-cyber-index/blob/main/reports/EMERGING-TECH-MISUSE-2026-10-07.md)
に、確認した事実とMithrilの分析を分けてまとめています。
