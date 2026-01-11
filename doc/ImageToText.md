# ImageToText.py 仕様

## 目的
画像ファイルパスを受け取り、メタ情報と Gemini API による簡易要約をテキストのリストとして返す。

## 関数
- `image_to_text(image_path: str, api_key: str | None = None) -> None`
  - 入力: 画像ファイルパス、任意で Gemini API キー（未指定時は環境変数 GEMINI_API_KEY を参照）。
  - 動作: 対応する JSON (`assets/imagetotext/<画像名>.json`) が既にあれば何もしない。無ければメタ情報と Gemini 要約を生成して JSON に書き出す。
  - エラー（例外送出）:
    - `ValueError`: パスが空
    - `FileNotFoundError`: ファイルが存在しない
    - `RuntimeError`: Pygame が画像を読めなかった場合

- `read_text_from_json(image_path: str) -> list[str]`
  - 入力: 画像ファイルパス。
  - 出力: 対応する JSON があればその配列を返す。なければ空リスト。

## 依存
- `pygame`
- `google-generativeai`（未導入時は要約をスキップ）
- 標準ライブラリ: `os`, `mimetypes`, `json`

## 拡張余地
- Gemini モデルの切り替えやプロンプト調整。
- OCR/タグ付けとの併用でキーワードリストを返す形への拡張。
