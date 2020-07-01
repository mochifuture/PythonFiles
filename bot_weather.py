# 天気予報コマンドを作成する
import requests

# 関数を作成する（定義する）
# def 関数名(): 英語のdefine（定義する）の略
def weather_command():
    base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
    # 東京の都市コードを指定
    query_params = {'city':'130010'}
    # urlを作成しデータを取得
    data = requests.get(base_url, params=query_params).json()
    # データが取得できてるか確認
    # print(data['title'])

    # botの応答を作成
    city = data['location']['city']
    date = data['forecasts'][0]['date']
    datelabel = data['forecasts'][0]['dateLabel']
    telop = data['forecasts'][0]['telop']

    response = '{}:{}の{}のお天気は「{}」です'.format(date, city, datelabel, telop)
    # 結果を返す
    return response