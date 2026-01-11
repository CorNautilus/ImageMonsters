# game.py 仕様

## 目的
アプリ全体のライフサイクルとシーン遷移・設定管理のハブ。

## 役割
- `constants` のサイズで Pygame (ウィンドウ/時計/フォント) を初期化する。
- シーン（現状は `TestScene`）を生成し、共有リソース（screen, clock, fonts）を渡す。
- `run()` でシーンの `run()` を起動し、終了後に `pygame.quit()` を行う。
- 将来的なタイトル/ホームなどのシーン切り替えや設定管理の起点とする。

## クラス
### `Game`
- **属性**
  - `screen`: `SCREEN_WIDTH/SCREEN_HEIGHT` サイズのメインサーフェス。
  - `scene`: 現在アクティブなシーンインスタンス（現状 `TestScene`）。
- **メソッド**
  - `__init__()`: Pygame 初期化、画面・時計・フォント生成、`TitleScene` を生成して保持。
  - `run() -> None`: シーンの `run()` を実行し、終了後に `pygame.quit()` を呼ぶ。
  - `_on_game()`: 「ゲーム」ボタン押下時のハンドラ（現状 print のみ）。
  - `_on_ai()`: 「AIテスト」押下時のハンドラ（print 後に `TestScene` を生成・実行）。

## 入出力
- 入力: なし（シーン側に委譲）。
- 出力: なし（シーン側に委譲）。

## 依存
- `pygame`
- ローカルモジュール: `constants`, `TestScene`

## エラーハンドリング
- シーンの中で実施（Game 自体は個別のエラーハンドリングを持たない）。
