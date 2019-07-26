path = 'data/hightemp.txt'
path_w = 'data/'

col1 = open(path_w + 'col1.txt', 'w')
col2 = open(path_w + 'col2.txt', 'w')

with open(path, 'r') as f :
  lines = f.readlines()
  for line in lines :
    tmp = list(line.split('\t'))
    col1.write(tmp[0] + '\n')
    col2.write(tmp[1] + '\n')

col1.close()
col2.close()