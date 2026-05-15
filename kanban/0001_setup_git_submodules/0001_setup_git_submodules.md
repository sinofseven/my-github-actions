# Gitサブモジュール（3つ）のセットアップ

## 目的
その先の情報を参照したいから

## 要望
gitのsubmoduleを作ってほしい

対象リポジトリ（それぞれ v1.0.0 を使用）:
- `git@github.com:sinofseven/action-request-id-token.git`
- `git@github.com:sinofseven/action-verify-jwt.git`
- `git@github.com:sinofseven/action-repository-dispatch.git`

## プラン
1. 3つのリポジトリを `git submodule add` で統合
2. 各リポジトリで v1.0.0 タグをチェックアウトしてピン留め
3. `.gitmodules` ファイルが生成される
4. サブモジュール設定を確認

## 完了サマリー
**完了日時**: 2026-05-15T18:30:15+09:00

タスク「Gitサブモジュール（3つ）のセットアップ」が完了しました。

### 実装内容
- 3つのGitHubリポジトリを サブモジュールとして追加しました
- 各サブモジュールで v1.0.0 タグにチェックアウトしました
- `.gitmodules` ファイルが生成されました

### 確認事項
- ✅ `action-request-id-token` が v1.0.0 でピン留めされている
- ✅ `action-verify-jwt` が v1.0.0 でピン留めされている
- ✅ `action-repository-dispatch` が v1.0.0 でピン留めされている
- ✅ `.gitmodules` ファイルに3つのサブモジュール設定が含まれている

### 次のステップ
- `git commit` で変更をコミット（ユーザーが明示的に指示した場合のみ）
- `git clone --recurse-submodules` でリポジトリをクローン可能になります
