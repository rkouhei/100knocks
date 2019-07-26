def cipher(target) :
  ans = ''
  for c in target :
    if c.islower() :
      ans += chr(219-ord(c))
    else :
      ans += c
  return ans

if __name__ == "__main__":
  print('文字列の入力 : ', end='')
  target = input()
  
  message1 = cipher(target)
  message2 = cipher(message1)
  print('暗号化 : ', message1)
  print('復号化 : ', message2)