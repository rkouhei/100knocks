path = 'data/hightemp.txt'

print('先頭行の表示')
print('N : ', end='')
N = int(input())

with open(path, 'r') as f :
  lines = f.readlines()
  for i in range(N) :
    print(lines[i], end='')