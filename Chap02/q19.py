import itertools as it
path = 'data/hightemp.txt'

# 都道府県名だけのリスト作成
first_row_list = []
with open(path, 'r') as f :
  lines = f.readlines()
  for line in lines :
    tmp = line.split('\t')
    first_row_list.append(tmp[0])

# 何回登場するかカウントし、リストに格納
first_row_list.sort()
gr = it.groupby(first_row_list)
ans = []
for key, group in gr :
  ans.append((key,len(list(group))))
ans.sort(key=lambda x: x[1], reverse=True)

for pref, cnt in ans :
  print(pref, cnt)