path = 'data/hightemp.txt'

with open(path, 'r') as f :
  lines = f.readlines()

  ans = []
  for line in lines :
    # print(line.replace('\t', ' '))
    ans.append(line.replace('\t', ' '))
  
  print(ans)