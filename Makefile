.PHONY: init setup update help

help:
	@echo "利用可能なコマンド:"
	@echo "  make init     - サブモジュールを初期化（clone直後に実行）"

init: setup

setup:
	git submodule update --init --recursive

.PHONY: \
	help \
	init \
	setup

