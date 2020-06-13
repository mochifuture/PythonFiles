bot_messages = {
  'こんにちは': 'Hello',
  'おはよう': 'Good Morning',
  'ありがとう': 'Thanks',
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
  print(response)
 
  # whileループ終了
  if 'さようなら' in command:
    break
