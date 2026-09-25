# pstack

プラグイン `~/.cursor/plugins/local/pstack` のコマンドと、この端末のモデル割り当て。2026-09-25 の写し。

ライブの割り当ては `~/.cursor/rules/pstack-models.mdc`。`install.sh` は `~/.cursor` を同期しない。`/setup-pstack` をやり直したら、このファイルの表も直す。頼まれない限り `/setup-pstack` は再実行しない。

## チャット欄とサブエージェント

チャット欄で選んだモデルは、その会話の親だけに効く。下の表は pstack が起動するサブエージェントのモデル。`inherit-parent` か `auto` と書いた役割は親と同じモデルになる。今のルールファイルにその2つは無い。

## 予算

`medium (high)`。量の多い実装は Grok と Composer。判断は Opus。Fast は書いていない。Fast は料金が2倍になり、品質は上がらない。

Opus は Other Models の従量になる。実装の既定を Opus に寄せない。

## 役割

| 役割 | モデル | 使うところ |
| --- | --- | --- |
| feature, refactoring | `grok-4.7-high` | 機能追加、リファクタ |
| bug-fix | `grok-4.7-high` | バグ修正 |
| perf-issue | `grok-4.7-high` | 速度の一回きりの修正 |
| hillclimb | `grok-4.7-high` | 指標を測りながらの改善 |
| judgment and prose | `claude-opus-5-5-high` | 判断と文章 |
| hardest tasks | `claude-opus-5-5-high` | 一番難しい実装 |
| how explorer | `grok-4.7-high` | `/how` の調査 |
| how explainer | `claude-opus-5-5-high` | `/how` の説明 |
| why investigators | `grok-4.7-high` | `/why` の調査 |
| why synthesizer | `claude-opus-5-5-high` | `/why` のまとめ |
| reflect tooling | `composer-2.5` | `/reflect` のツール側 |
| reflect judgment, divergent, synthesizer | `claude-opus-5-5-high` | `/reflect` の判断 |
| arena runners | `grok-4.7-high`, `composer-2.5` | `/arena` の候補。2体 |
| arena cross-judge pool | `claude-opus-5-5-high`, `grok-4.7-high` | 親と別ファミリーを1つ選ぶ |
| swarm workers | `composer-2.5` | `/swarm` の作業者 |
| architect runners | `claude-opus-5-5-high`, `grok-4.7-high` | `/architect` の並列。2体 |
| interrogate reviewers | `claude-opus-5-5-high`, `grok-4.7-high` | `/interrogate` のレビューア。2体 |

行を消すと、その役割はスキル側の既定に戻る。

## 打つコマンド

普段の実装は `/poteto-mode`。仕事の種類はエージェントが選ぶ。下のプレイブック名はスラッシュコマンドではない。

調べる。

- `/how`。動き、置き場所、どの層が持つか。
- `/why`。なぜそうなっているか。根拠を引く。
- `/recall`。最近の作業を短く戻す。
- `/teach`。`/how` と `/why` を一つの説明にまとめる。
- `/bro`。直前の文を、専門語なしで言い直す。

設計を広げる。判断役は Opus になる。

- `/architect`。コードの前に型とモジュールを置く。
- `/arena`。同じ課題の候補を並べ、強いところを一つに継ぐ。
- `/swarm`。並列の作業者に分けて、一つの報告に戻す。
- `/interrogate`。複数モデルで差分を突く。anpic のレビューでは使わない。
- `/reflect`。今のチャットから、既存スキルへの修正を出す。
- `/figure-it-out`。狭いプレイブックが無い大きな仕事の手順を作る。

文章と差分。

- `/technical-writing`。ドキュメント、README、PR 文、コミットメッセージ。
- `/unslop`。文章から AI の癖を落とす。文章を書くときはエージェントが自分で適用する。
- `/no-comments`。コメントの要否を見る。anpic の frontend export の TSDoc は剥がさない。
- `/blast-radius`。差分の外で壊れそうな箇所を、実行して確認する。
- `/tdd`。失敗するテストから書く。頼んだときだけ。
- `/show-me-your-work`。長い作業の判断を1行ずつ残す。

モデルと、自分のやり方。

- `/setup-pstack`。上の表を書き直す。可用モデルを見て `~/.cursor/rules/pstack-models.mdc` を上書きする。
- `/automate-me`。自分の作業の癖を個人スキルにする。
- `/create-verification-skill`。そのリポジトリ用に、画面や CLI を操作して確認するスキルを作る。
- `/maintain-verification-skill`。その確認スキルが実装とずれていないか見る。
- `/make-bot-ui`。Webhook で Grok Bot を起こす画面を作る。

打たないもの。

- `typescript-best-practices`。`.ts` と `.tsx` を触ると適用される。
- `principle-*`。`/poteto-mode` が必要なときだけ読む原則。コマンドではない。

## anpic での割り当て

anpic の個人ルール（git では追跡しない）での分け方。

| 役割 | 使うもの |
| --- | --- |
| 設計・実装 | `/poteto-mode` |
| 検証 | `/poteto-mode` の検証、テストと lint |
| レビュー | thermos の `/thermos` |

`/thermos` は差分の監査と、保守性の監査を並行に起動する。`/thermo-nuclear-review` は監査だけ、`/thermo-nuclear-code-quality-review` は保守性だけ。

anpic では pstack の shipping、autopilot、orchestrate で merge や push をしない。

## `/poteto-mode` が選ぶ仕事

スラッシュでは打たない。仕事に合うものをエージェントが開く。

- Feature。新しい振る舞い。
- Refactoring。振る舞いを変えずに形を変える。
- Bug fix。再現して直す。
- Perf issue。遅さを一度直す。
- Hillclimb。一つの指標を測りながら上げる。
- Investigation。読み取りの質問。
- Prototype。捨てるスケッチで決める。
- Visual parity。見た目を揃える。
- Authoring a skill。`SKILL.md` を書く。
- Eval。スキルやプロンプトの効きを見る。
- Runtime forensics。動いている症状の診断。
- Trace forensics。渡されたプロファイルの診断。
- Babysit。PR をマージできる状態まで進める。
- Shipping。緑のスタックを下から積む。
- Opening a PR。他のプレイブックの終わりに PR を開く。
- Autonomous run。一つの仕事を条件まで進める。
- Orchestrate。複数日、複数 PR のプログラム。
- Autopilot-full。独立した PR をマージまで進める。
- Autopilot-stack。レビュー用の積み重ねにして、マージは人間が行う。
- Session pickup。前のエージェントの途中から再開する。
- Pause safely。途中で止めて再開できるようにする。
- Multi-phase plan。段階や積み重ねにまたがる計画。
- Worktree cleanup。マージ済みの worktree と古いシミュレータを捨てる。
