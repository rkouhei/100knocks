path = 'data/hightemp.txt'

sort_list = []
with open(path, 'r') as f :
  lines = f.readlines()
  for line in lines :
    tmp = line.split('\t')
    sort_list.append(tmp)

sort_list.sort(key=lambda x: float(x[2]), reverse=True)
# print(sort_list)

for line in sort_list :
  print('\t'.join(line), end='')