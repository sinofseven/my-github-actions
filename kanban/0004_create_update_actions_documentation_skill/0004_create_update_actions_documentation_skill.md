# アクション説明更新スキルを作成する

## 目的

今後もアップデート作業をやるので skill-creatorを使ってこのリポジトリに新しいスキルとして作ってほしい。

## 要望

0002, 0003でやった内容を一つのスキルにまとめて。

## 完了サマリー

**完了日時：** 2026-05-15T11:30:00+09:00

### 実施内容

1. **スキル定義ファイル（SKILL.md）を作成**
   - スキル名：`update-actions-documentation`
   - GitHub Actionsサブモジュール更新時にREADMEを自動生成/更新するスキル
   - 主な機能と使用方法を記載

2. **スキル実装スクリプト（update_readme.py）を作成**
   - ActionDocumentationGeneratorクラスで実装
   - .gitmodulesを読んでサブモジュール情報を抽出
   - 各サブモジュールのREADMEからアクション情報を抽出
   - README.md（日本語版）とREADME_en.md（英語版）を自動生成
   - 各パラメータに[Required/Optional]ラベルと説明コメントを追加

3. **スキル構造を確立**
   - ディレクトリ：`.claude/skills/update-actions-documentation/`
   - SKILL.md - スキル定義
   - scripts/update_readme.py - 実装スクリプト

### 0002・0003の作業を統合

- **0002の作業**（README更新）→ `generate_readme_japanese()` と `generate_readme_english()`
- **0003の作業**（コメント追加）→ パラメータ情報の埋め込みと置換処理

### スキルの成果物

- `/Users/yuta/space/private/my-github-actions/.claude/skills/update-actions-documentation/SKILL.md`
- `/Users/yuta/space/private/my-github-actions/.claude/skills/update-actions-documentation/scripts/update_readme.py`
- `/Users/yuta/space/private/my-github-actions/kanban/0004_create_update_actions_documentation_skill/log.md`

### 今後の利用

このスキルを使用することで、アクションの説明や使用例を更新する際に、README.mdとREADME_en.mdを自動的に生成・更新できるようになった。
