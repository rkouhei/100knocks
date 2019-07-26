path = 'data/hightemp.txt'

with open(path, 'r') as f :
  lines = f.readlines()
  print(len(lines))