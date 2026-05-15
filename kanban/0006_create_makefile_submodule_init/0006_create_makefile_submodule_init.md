# Makefile作成とサブモジュール初期化

## 目的
submoduleの有効化手順を忘れることが多いから

## 要望
Makefileを作成し、clone直後にsubmoduleを初期化するコマンドを書いてください

## プラン
ルートディレクトリに Makefile を作成し、以下のコマンドを提供：
- `make init / make setup`: git submodule update --init --recursive を実行
- `make update`: git submodule update --remote --recursive を実行
- `make help`: 利用可能なコマンドを表示

## 完了サマリー
**完了日時**: 2026-05-15T14:35:00+09:00

### 実装内容
- Makefile を新規作成（ルートディレクトリ）
- `make init / make setup`: サブモジュール初期化コマンド
- `make update`: サブモジュール更新コマンド
- `make help`: ヘルプ表示コマンド

### テスト結果
- ✓ `make help`: コマンド一覧表示が正常に動作
- ✓ `make init`: サブモジュール初期化が正常に実行

詳細はログファイル `log.md` を参照
