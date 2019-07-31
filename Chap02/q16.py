path = 'data/hightemp.txt'
print('末尾の表示')
print('N : ', end='')
N = int(input())

with open(path, 'r') as f :
  lines = f.readlines()
  cnt = len(lines)
  x = 1 if cnt%N > 0 else 0
  dvd = cnt // N + x
  for i in range(dvd) :
    path_n = 'data/q16_output_' + str(i) + '.txt'
    with open(path_n, 'w') as fn:
      tmp = ''.join(lines[N*i:N*(i+1)])
      fn.write(tmp)