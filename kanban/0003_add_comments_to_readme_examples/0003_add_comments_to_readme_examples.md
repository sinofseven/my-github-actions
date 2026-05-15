# READMEの使用例に詳細なコメントを追加する

## 目的

ここのREADMEさえ読めばある程度使えるようにしたい。

## 要望

READMEのexampleで各設定値に対してコメントを追記して。

## 完了サマリー

**完了日時：** 2026-05-15T10:45:00+09:00

### 実施内容

1. **README.md（日本語版）を更新**
   - 3つのアクション（action-request-id-token、action-verify-jwt、action-repository-dispatch）の使用例にコメントを追記
   - 各パラメータに [Required/Optional] と説明を記載

2. **README_en.md（英語版）を更新**
   - 日本語版と同じ構成で英語版を更新
   - 各パラメータの説明を英語で記載

### 成果物

- `/Users/yuta/space/private/my-github-actions/README.md` - 更新完了
- `/Users/yuta/space/private/my-github-actions/README_en.md` - 更新完了
- `/Users/yuta/space/private/my-github-actions/kanban/0003_add_comments_to_readme_examples/log.md` - 作業ログ記録完了

### 改善内容

- READMEの使用例が、各パラメータの説明とともにより詳細になった
- [Required/Optional]の表記により、ユーザーが必須パラメータとオプショナルパラメータを区別しやすくなった
- READMEだけで各アクションの基本的な使い方が理解できるようになった
