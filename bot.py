# 天気コマンドをインポート
from bot_weather import weather_command

bot_messages = {
  'こんにちは': 'Hello',
  'おはよう': 'Good Morning',
  'ありがとう': 'Thanks',
  'ありがとう': 'Thanks',
  'ほげ': 'hogehoge',
  'こんばんは': 'Good Evening',
  'おやすみ': 'Good Night',
  'さようなら': 'Bye'
}

while True:
  command = input('はなしかける>')
  response = ''

  for key in bot_messages:
    if key in command:
      response = bot_messages[key]
      break

  # bot_messagesにない文字列が入力された時の返答
  if not response:
    response = 'わからない'

  # 天気コマンドを追加
  if '天気' in command:
    response = weather_command()

  print(response)
 
  # whileループ終了
  if 'さようなら' in command:
    break
