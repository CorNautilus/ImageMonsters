# constants.py 仕様

## 目的
Pygame ビューア用の定数を一元管理する。

## 内容
- `SCREEN_WIDTH = 960`
- `SCREEN_HEIGHT = 600`
- `FPS = 60`
- 色: `BG_COLOR`, `PANEL_COLOR`, `TEXT_COLOR`, `BUTTON_COLOR`, `BUTTON_HOVER_COLOR`

## 使い方
- 他モジュールがインポートし、サイズ・時間・配色を統一する。

## エラーハンドリング
- 静的値のみで特別な処理はなし。
