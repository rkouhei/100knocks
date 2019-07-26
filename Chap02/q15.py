path = 'data/hightemp.txt'

print('末尾の表示')
print('N : ', end='')
N = int(input())

with open(path, 'r') as f :
  lines = f.readlines()
  cnt = len(lines)
  for i in range(N) :
    print(lines[cnt-N+i], end='')