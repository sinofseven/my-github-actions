# action-workflow-dispatch のサブモジュール追加

## 目的
新しいアクションを書いたから追加したい

## 要望
`git@github.com:sinofseven/action-workflow-dispatch.git` をサブモジュールとして追加して最新バージョンのタグにして

## プラン
- git submodule add で action-workflow-dispatch をサブモジュール追加
- git checkout v1.0.0 で最新タグにチェックアウト
- .gitmodules の確認（自動更新）
- README.md と README_en.md にアクション説明を追加
- 既存 3 つのアクションと同じドキュメント構造を採用

## 完了サマリー

**完了日時**: 2026-05-17T17:15:00+09:00

### 実装完了内容

1. **サブモジュール追加**
   - `git submodule add git@github.com:sinofseven/action-workflow-dispatch.git action-workflow-dispatch` を実行
   - `v1.0.0` タグにチェックアウト（commit d14f3b5）
   - `.gitmodules` に自動追加

2. **ドキュメント更新**
   - `README.md` に日本語説明を追加
   - `README_en.md` に英語説明を追加
   - 既存 3 つのアクション説明と同じ構造に統一

3. **動作確認**
   - `make init` でサブモジュール初期化が成功
   - `git status` で変更内容を確認

### 変更ファイル
- `.gitmodules` (modified)
- `README.md` (modified)
- `README_en.md` (modified)
- `action-workflow-dispatch/` (new submodule)

### 詳細ログ
[log.md](log.md) を参照
