# 常にTrue（正）でプログラムを繰り返し処理する
while True:
  # 入力をおうむ返しする
  command = input('はなしかける>')

  # in演算子
  if 'こんにちは' in command:
      print('いいお天気ですね')
  elif 'おしまい' in command:
      print('さようなら')
      break
  else:
     print(command)