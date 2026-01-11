# TestScene.py 仕様

## 目的
シンプルな画像ビューアシーン。`assets/` の画像を読み込み、前/次ボタンで巡回表示する。

## 役割
- Game から渡された共有リソース（screen, clock, fonts）を使って描画・入力処理を行う。
- `assets/` の画像をロードし、インデックスを管理する。
- 毎フレームの描画とイベント処理（QUIT/左クリック）を担当する。

## クラス
### `TestScene`
  - `screen`: 描画先の Pygame サーフェス。
  - `clock`: FPS 制御用の Pygame Clock。
  - `font`, `title_font`: テキスト描画用フォント。
  - `images`: 読み込んだ画像サーフェスのリスト。
  - `current_index`: 現在表示している画像インデックス（画像なしは -1）。
  - `buttons`: 「前へ」「次へ」ボタンの定義と矩形。
  - `__init__(screen, clock, font, title_font)`: リソースを受け取り、画像読込とボタン設定を行う（前へ/次へ/参照）。
  - `_load_assets_images() -> list[pygame.Surface]`: `assets/images/` の png/jpg/jpeg/webp をソートして読み込み、最大 860x400 に収まるようアスペクト比を維持してスケールしてリスト化。
  - `run() -> None`: メインループ。QUIT と左クリックを処理し、背景塗り→レイアウト描画→flip→FPS tick。
  - `_draw_layout(mouse_pos, mouse_down) -> None`: タイトル、表示パネル、画像（存在時は枚数インジケータ付き）を描画。前/次ボタンで巡回、参照ボタンで画像選択をトリガー。
  - `_choose_and_add_image() -> None`: ファイルダイアログで画像を選択し、`assets/images/` に `image01`, `image02` ... の連番で保存してから読み込み、リストへ追加して表示する。

## 入出力
- 入力: `assets/` の画像ファイル、マウスイベント。
- 出力: 画面への描画のみ。

## 依存
- `pygame`
- ローカルモジュール: `assets`, `ui`, `constants`

## エラーハンドリング
- `assets/` 不在や空の場合: 「画像がありません」メッセージを表示。
- 画像読み込み失敗: `assets.load_image` のプレースホルダで代替。
