# ui.py 仕様

## 目的
背景・パネル・テキスト・ボタンを描くための再利用可能ヘルパー。

## 役割
- `constants` のカラーパレットを用いたシンプルなUI描画処理を集約する。

## 関数
- `fill_background(surface)`: 背景色と外枠を描画。
- `draw_panel(surface, rect)`: 角丸パネルと枠線を描画。
- `draw_text(surface, text, pos, font, color=TEXT_COLOR) -> Rect`: テキストを描画し Rect を返す。
- `draw_button(surface, rect, text, font, mouse_pos, mouse_down) -> bool`: ホバー時に色を変えるボタンを描画。ホバーかつクリック時に True を返す。

## 入出力
- 入力: Pygame サーフェス、矩形情報、マウス状態。
- 出力: サーフェスへの描画、ボタンのクリック判定（bool）。

## 依存
- `pygame`
- `constants`（色設定）

## エラーハンドリング
- 有効なサーフェス/Rect 前提で特別なエラーハンドリングは行わない。
