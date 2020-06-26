# requestsライブラリを使うためimportする
import requests

# requestsのget()メソッドで任意のWebページの情報を取得
response = requests.get('https://www.yahoo.co.jp/')

# Webサイトにアクセスした結果を表す数値「ステータスコード」
# 成功は「200」
# Webページが存在しない時は「404」
print(response.status_code)

# HTMLの先頭500文字を表示
print(response.text[:500])