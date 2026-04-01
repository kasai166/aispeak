# aispeak

VOICEVOXとGemini APIを連携させた、AIとの音声対話プログラムのリポジトリです。

## 概要
ユーザーの声をマイクから入力し、Gemini APIで生成した回答をVOICEVOXで読み上げます。
過去に作成したAPI連携プログラムの経験を活かし、音声認識・生成AI・音声合成の3つの要素を統合する練習として作成しています。
またAPIを用いたプログラムを作成してみたいと当時考え作成を行ったもののため練習プログラムとなります。
今後時間のある時に感情分析を追記しよりリアルなものの作成を行いたいと考えています。

## 機能
- **音声認識 (speakin.py)**: `speech_recognition` を使用してマイク入力を日本語テキストに変換します。
- **思考 (geminitalk.py)**: Gemini 1.5 Flash モデルを使用して、入力に対する回答を生成します。
- **音声合成 (speakout.py)**: VOICEVOX Engineを介して、生成されたテキストを音声として再生します。
- **メイン制御 (main.py)**: 上記の機能を組み合わせた対話ループを管理します。

## 構成図
1. **入力**: マイクからユーザーの声を取得 (Speech Recognition)
2. **処理**: テキストをGemini APIへ送信 (Gemini 1.5 Flash)
3. **出力**: 回答テキストをVOICEVOXへ送信し、スピーカーから再生 (VOICEVOX API)

## 必要要件
- Python 3.x
- **VOICEVOX Engine**: ローカルで起動している必要があります（デフォルト: `127.0.0.1:50021`）。
- **Gemini API Key**: Google AI Studioから取得したAPIキーが必要です。(過去に作成した物のためgemini1.5flashを設定している為現行で利用できるmodelの指定を各自行ってください)

### 必要なライブラリ
```bash
pip install google-generativeai requests sounddevice numpy SpeechRecognition
# マイク入力の制御に必要になる場合があります
pip install PyAudio