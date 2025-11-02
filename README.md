# 天気予報プログラム

OpenWeatherMap APIを使用して、指定した都市の現在の天気を取得・表示するPythonプログラムです。

## 機能

- 指定した都市の天気情報を取得
- 気温（摂氏）、体感温度の表示
- 湿度、風速の表示
- 天気の説明（日本語）
- コマンドライン引数で都市を指定可能
- エラーハンドリング

## 必要な環境

- Python 3.7以上
- pip（Pythonパッケージマネージャー）

## セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. OpenWeatherMap APIキーの取得

1. [OpenWeatherMap](https://openweathermap.org/api)にアクセス
2. 無料アカウントを作成（Sign upから）
3. API Keysセクションでキーを取得（数分で有効化されます）

### 3. 環境変数の設定

`.env.example`をコピーして`.env`ファイルを作成：

```bash
cp .env.example .env
```

`.env`ファイルを編集して、取得したAPIキーと都市名を設定：

```env
OPENWEATHER_API_KEY=あなたのAPIキー
CITY=Tokyo
```

## 使い方

### 基本的な使い方

デフォルト都市（.envで設定した都市またはTokyo）の天気を取得：

```bash
python weather_forecast.py
```

### コマンドライン引数で都市を指定

```bash
python weather_forecast.py --city Osaka
```

または、uvを使用する場合：

```bash
uv run python weather_forecast.py --city Osaka
```

### ヘルプの表示

```bash
python weather_forecast.py --help
```

## 実行例

```
Tokyoの天気を取得中...

==================================================
📍 Tokyo, JP の天気
🕐 取得時刻: 2025-11-02 18:54:37
==================================================
☁️  天気: 曇りがち
🌡️  気温: 15.2°C
🤔 体感温度: 14.8°C
💧 湿度: 72%
💨 風速: 3.5 m/s
==================================================
```

## 設定

`.env`ファイルで以下の設定が可能です：

- `OPENWEATHER_API_KEY`: OpenWeatherMap APIキー（必須）
- `CITY`: 取得したい都市名（デフォルト: Tokyo）

### 都市名の指定方法

都市名は以下の優先順位で決定されます：

1. コマンドライン引数 `--city`（最優先）
2. 環境変数 `CITY`（.envファイル）
3. デフォルト値（Tokyo）

### 都市名の例

- Tokyo
- Osaka
- Kyoto
- Fukuoka
- Sapporo
- London
- New York
- Paris

## ファイル構成

```
.
├── .env                # 環境変数（gitignoreされています）
├── .env.example        # 環境変数のテンプレート
├── .gitignore          # Git除外設定
├── README.md           # このファイル
├── requirements.txt    # 依存パッケージリスト
└── weather_forecast.py # メインプログラム
```

## 注意事項

- `.env`ファイルにはAPIキーが含まれるため、gitにコミットしないでください（.gitignoreに設定済み）
- OpenWeatherMapの無料プランでは、1分間に60回までのAPI呼び出し制限があります
- APIキーが有効化されるまで数分かかる場合があります

## ライセンス

MIT License
