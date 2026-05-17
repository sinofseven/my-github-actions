# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

GitHub Composite Actions のコレクションリポジトリ。各アクションは独立した GitHub リポジトリとして管理され、**git サブモジュール**としてこのリポジトリに含まれている。

## Setup

```bash
make init  # サブモジュールを初期化（clone直後に必須）
```

内部では `git submodule update --init --recursive` を実行している。

## Architecture

### サブモジュール構成

各アクションは独自リポジトリ (`sinofseven/<action-name>`) であり、このリポジトリではバージョンタグで固定したサブモジュールとして管理する。

| サブモジュール | バージョン | 概要 |
|---|---|---|
| `action-request-id-token` | v1.0.1 | GitHub OIDC IDトークン取得 |
| `action-verify-jwt` | v1.1.0 | JWKS を使ったJWT検証（Linux x86_64のみ） |
| `action-repository-dispatch` | v1.0.1 | 別リポジトリへ `repository_dispatch` 送信 |
| `action-workflow-dispatch` | v1.0.0 | 別リポジトリの `workflow_dispatch` トリガー |

各サブモジュールは以下の構造を持つ：
- `action.yml` — Composite Action の定義（inputs/outputs/steps）
- `README.md` — 英語ドキュメント

### ドキュメント管理

`README.md`（日本語）と `README_en.md`（英語）はサブモジュールの `README.md` から自動生成する。

**更新方法：** `update-actions-documentation` スキルを使用する。サブモジュールを追加・更新した後にこのスキルを実行すると、両方の README が同期される。

ドキュメントの規約：
- 使用例のインラインコメントに `[Required]` / `[Optional]` ラベルを付与する
- 日本語版と英語版で内容・構成を一致させる

### サブモジュールのバージョン更新

**推奨：** `update-submodules` スキルを使用する。リモートの最新タグを自動検出し、更新候補を提示した上で `git checkout` まで実行する。

手動で行う場合：
1. タグを指定して `git -C <submodule-name> checkout <tag>`
2. `git add <submodule-name>` でサブモジュールのコミットハッシュを更新
3. `update-actions-documentation` スキルでREADMEを同期

### タスク管理（Kanban）

作業は `kanban/` ディレクトリでKanbanスタイルで管理する（`kanban-kit` プラグインを使用）。
- タスクファイル: `kanban/{NNNN}_{title}/{NNNN}_{title}.md`
- 作業ログ: `kanban/{NNNN}_{title}/log.md`

## 利用可能なスキル

| スキル | 用途 |
|---|---|
| `update-submodules` | サブモジュールのリモート最新タグを確認し、更新を実行 |
| `update-actions-documentation` | サブモジュール追加・更新後に README.md / README_en.md を同期 |
| `commit` | ステージ済み変更からコミットメッセージを生成してコミット |
| `kanban-kit:kanban` | kanban タスクを実行 |
| `kanban-kit:add-kanban` | 新規 kanban タスクを作成 |

## Constraints

- `action-verify-jwt` は **Linux x86_64** (`ubuntu-*`) ランナーのみ対応。macOS/Windows は非対応。
- 各アクションは Composite Action（YAML定義）であり、ビルド・コンパイル工程は不要。
