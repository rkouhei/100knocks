def n_gram(target, size) :
  ans = [target[x:x+size] for x in range(len(target)-size+1)]
  return ans


if __name__ == "__main__" :
  target = 'I am an NLPer'
  # print(n_gram(target,1))
  print(n_gram(target,2))
  # print(n_gram(target,3))