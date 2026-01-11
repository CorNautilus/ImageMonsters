# ImageMonsters Pygame Viewer - Module Specs

## Overview
シンプルな画像ビューア。assets フォルダに置いた画像を読み込み、前へ/次へで巡回表示する。

## Modules
- constants.py
  - 画面サイズ、FPS、背景色・パネル色・文字色・ボタン色を定義する定数置き場。
  - 他モジュールは色や解像度をここから参照するだけで、状態は持たない。

- assets.py
  - load_image(path, size): ファイルを読み込み指定サイズへスケール。存在しない場合はプレースホルダ画像を返す。
  - 依存: pygame, constants.PANEL_COLOR。

- ui.py
  - fill_background(surface): 背景と枠線を描画。
  - draw_panel(surface, rect): パネル枠を描画。
  - draw_text(surface, text, pos, font, color=TEXT_COLOR): テキスト描画。
  - draw_button(surface, rect, text, font, mouse_pos, mouse_down): ボタン描画し、ホバーかつクリック時に True を返す。
  - 依存: constants の色設定。

- game.py
  - Game クラスがアプリ全体を司るハブ。
    - __init__: 画面初期化、フォント準備、`TestScene` を生成して保持。
    - run: 現在のシーンの run を呼び、終了時に pygame.quit を実行。
  - 依存: constants の解像度/FPS、TestScene。

- TestScene.py
  - シンプルな画像ビューアシーン。
    - _load_assets_images: assets ディレクトリの png/jpg/jpeg/webp をソートして読み込み、最大 860x400 に収まるようアスペクト比を維持してスケール。
    - run: メインループ。イベント処理→描画→FPS 制御。ウィンドウ閉じると終了。
    - _draw_layout: タイトル、表示パネル、画像（存在時は枚数インジケータ付き）を描画。前/次ボタンで巡回、参照ボタンで画像選択をトリガー。
    - _choose_and_add_image: ファイルダイアログで画像を選択し、そのまま読み込んでリストへ追加して表示（保存なし）。
  - 依存: assets.load_image, ui の描画関数群, constants。

- main.py
  - エントリーポイント。Game を生成し run を呼ぶのみ。

## User Flow
1) 起動すると assets 配下の画像を読み込み、先頭を表示。
2) 「前へ」「次へ」ボタンで画像インデックスを循環変更。
3) assets に画像が無い場合は「assets フォルダに画像がありません」と表示。

## I/O と前提
- 入力: assets フォルダの画像ファイル (png/jpg/jpeg/webp)。
- 出力: 画面への表示のみ。ファイル書き込みなし。
- 前提: pygame がインストール済み。assets フォルダが存在（空でも可）。
