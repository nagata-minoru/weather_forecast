#!/usr/bin/env python3
"""
天気予報を取得して表示するプログラム
OpenWeatherMap APIを使用
"""

import os
import requests
import argparse
from datetime import datetime
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

def get_weather(city_name, api_key):
  """
  指定された都市の天気情報を取得

  Args:
    city_name: 都市名（例: Tokyo, Osaka）
    api_key: OpenWeatherMap APIキー

  Returns:
    天気情報の辞書、エラーの場合はNone
  """
  base_url = "http://api.openweathermap.org/data/2.5/weather"

  # APIリクエストパラメータ
  params = {
    "q": city_name,
    "appid": api_key,
    "units": "metric",  # 摂氏温度
    "lang": "ja"  # 日本語
  }

  try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # エラーチェック
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"エラー: APIリクエストに失敗しました - {e}")
    return None

def display_weather(weather_data):
  """
  天気情報を見やすく表示

  Args:
    weather_data: get_weather()から取得した天気情報
  """
  if not weather_data:
    return

  # 天気情報を抽出
  city = weather_data["name"]
  country = weather_data["sys"]["country"]
  weather_desc = weather_data["weather"][0]["description"]
  temp = weather_data["main"]["temp"]
  feels_like = weather_data["main"]["feels_like"]
  humidity = weather_data["main"]["humidity"]
  wind_speed = weather_data["wind"]["speed"]

  # 現在時刻
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  # 結果を表示
  print("\n" + "="*50)
  print(f"📍 {city}, {country} の天気")
  print(f"🕐 取得時刻: {now}")
  print("="*50)
  print(f"☁️  天気: {weather_desc}")
  print(f"🌡️  気温: {temp}°C")
  print(f"🤔 体感温度: {feels_like}°C")
  print(f"💧 湿度: {humidity}%")
  print(f"💨 風速: {wind_speed} m/s")
  print("="*50 + "\n")

def main():
  """
  メイン処理
  """
  # コマンドライン引数をパース
  parser = argparse.ArgumentParser(description="指定された都市の天気予報を取得します")
  parser.add_argument(
    "--city",
    type=str,
    help="都市名（例: Tokyo, Osaka, Kyoto）"
  )
  args = parser.parse_args()

  # 環境変数から設定を取得
  API_KEY = os.getenv("OPENWEATHER_API_KEY")

  # 都市名の優先順位: コマンドライン引数 > 環境変数 > デフォルト値
  CITY = args.city or os.getenv("CITY", "Tokyo")

  if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
    print("エラー: APIキーを設定してください")
    print("1. https://openweathermap.org/api でアカウントを作成")
    print("2. APIキーを取得")
    print("3. .envファイルのOPENWEATHER_API_KEYを更新")
    return

  print(f"{CITY}の天気を取得中...")
  weather_data = get_weather(CITY, API_KEY)

  if weather_data:
    display_weather(weather_data)

if __name__ == "__main__":
  main()
