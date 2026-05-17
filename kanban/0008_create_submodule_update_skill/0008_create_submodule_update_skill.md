# サブモジュール自動更新スキルの開発

## 目的
手動で変更するのが大変なので

## 要望
各サブモジュールの最新バージョンを調べて、更新があればサブモジュールを最新バージョンに更新するスキルを作って。gitコマンドを駆使してやって欲しい

## プラン

`.claude/skills/update-submodules/SKILL.md` を新規作成する。

スキルの手順：
1. `.gitmodules` を読み、サブモジュール一覧を取得
2. 各サブモジュールについて `git fetch --tags` → 現在タグと最新リモートタグを比較
3. 更新候補をユーザーに提示して確認を取る
4. 承認後、各サブモジュールを `git checkout <latest-tag>` で更新
   （`git add` はスキルの範囲外。ユーザーが手動で実施）
5. 更新サマリーを報告し、次のステップを案内する

## 完了サマリー

**完了日時:** 2026-05-17T18:50:25+09:00

`.claude/skills/update-submodules/SKILL.md` を新規作成した。

スキルの機能：
- `.gitmodules` からサブモジュール一覧を自動取得
- `git ls-remote --tags origin` でリモートの最新タグを確認
- `git describe --tags --exact-match HEAD` で現在タグと比較
- 更新候補をユーザーに提示して確認を取ってから `git checkout` で更新
- `git add` は範囲外とし、ユーザーに次のステップを案内する

作成ファイル：
- `.claude/skills/update-submodules/SKILL.md`
