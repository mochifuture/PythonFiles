# requestsパッケージを使って天気予報の情報を取得する
# requestsライブラリを使うためimport
import requests

# Web API (Application Programming Interface)の利用S
# livedoorがWebAPIとして提供している「お天気Webサービス」から情報を取得する
# ベースURL 
# cityパラメータ city
# 都市コード 130010(東京)
response = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')

# Webサイトにアクセスした結果を表す数値「ステータスコード」
# 成功は「200」
# Webページが存在しない時は「404」
print(response.status_code)

# json()メソッドを利用してjsonフォーマットを取得
# json = JavaScript Object Notionフォーマットというデータ形式
# Pythonのdictionary（辞書）型のようなもの
data = response.json()
print(data)
# 今日の分だけ
# print(data['forecasts'][0])