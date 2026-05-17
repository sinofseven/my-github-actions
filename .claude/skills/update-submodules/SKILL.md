---
name: update-submodules
description: |
  各サブモジュールの最新バージョンをリモートから調べ、更新があればサブモジュールを最新タグに更新するスキル。

  以下の場合に使用する：
  - サブモジュールの最新バージョンを確認したいとき
  - サブモジュールを最新バージョンに更新したいとき
  - 「サブモジュールを更新して」「最新バージョンに上げて」と言われたとき

  このスキルは my-actions リポジトリ用（GitHub Actions コレクション）。
---

# update-submodules Skill

## Overview

`.gitmodules` に登録されているすべてのサブモジュールについて、リモートの最新タグを調べて現在のバージョンと比較し、更新があれば `git checkout` で最新タグに切り替える。

## 手順

### ステップ 1: サブモジュール一覧の取得

リポジトリルートの `.gitmodules` を読み、サブモジュールのパス一覧を取得する。

```bash
# .gitmodules からパスを抽出する例
grep "path = " .gitmodules | awk '{print $3}'
```

### ステップ 2: 各サブモジュールの現在バージョンとリモート最新タグを確認

各サブモジュールについて以下を実行する：

```bash
# リモートの最新タグを取得
LATEST=$(git -C <path> ls-remote --tags origin 2>/dev/null \
  | grep -v "\^{}" \
  | awk '{print $2}' \
  | sed 's|refs/tags/||' \
  | sort -V \
  | tail -1)

# 現在チェックアウトされているタグを確認
CURRENT=$(git -C <path> describe --tags --exact-match HEAD 2>/dev/null || echo "unknown")
```

- `CURRENT` と `LATEST` を比較し、異なれば更新候補としてリストに追加する
- `LATEST` が空（タグなし）の場合はそのサブモジュールをスキップする

### ステップ 3: 更新候補をユーザーに提示して確認

更新候補がある場合、AskUserQuestion を使って以下のような確認を取る：

```
以下のサブモジュールに更新があります：
- action-request-id-token: v1.0.0 → v1.0.1
- action-repository-dispatch: v1.0.0 → v1.0.1

更新しますか？
```

更新候補がない場合は「すべてのサブモジュールは最新バージョンです」と報告してスキルを終了する。

### ステップ 4: サブモジュールの更新

ユーザーが承認した場合、各更新候補について以下を実行する：

```bash
# リモートのタグを取得してからチェックアウト
git -C <path> fetch --tags
git -C <path> checkout <LATEST>
```

**注意:** `git add <path>` はこのスキルの範囲外。更新後にユーザーが手動で実行する。

### ステップ 5: 完了報告と次のステップ案内

更新結果をサマリーとして報告する：

```
更新完了：
- action-request-id-token: v1.0.0 → v1.0.1
- action-repository-dispatch: v1.0.0 → v1.0.1

次のステップ：
1. git add <各サブモジュールパス> でサブモジュールのコミットハッシュをステージング
2. /update-actions-documentation を実行して README を同期
3. /commit でコミット
```

## 注意事項

- このスキルは各サブモジュールの `checkout` のみ実行する。親リポジトリへの `git add` はユーザーが手動で行う
- タグが存在しないサブモジュールは更新対象外
- バージョン比較には `sort -V`（バージョン順ソート）を使用する
