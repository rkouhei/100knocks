import random

def Typoglycemia(target) :
  char_list = target.split(' ')
  ans = []

  for c in char_list :
    if len(c) <= 4 :
      ans.append(c)
    else :
      tmp = ''
      tmp += c[0]
      sr = c[1:-1]
      sr = ''.join(random.sample(sr,len(sr)))
      tmp += sr
      tmp += c[-1]
      ans.append(tmp)

  ans_str = ' '.join(ans)
  return ans_str

if __name__ == '__main__' :
  target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
  print(Typoglycemia(target))