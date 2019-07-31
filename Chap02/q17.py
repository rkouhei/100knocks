path = 'data/hightemp.txt'
w_path = 'data/q17_output.txt'

first_row_list = []
with open(path, 'r') as f :
  lines = f.readlines()
  for line in lines :
    tmp = line.split('\t')
    first_row_list.append(tmp[0])

first_row_list = list(set(first_row_list))
with open(w_path, 'w') as f :
  f.write('\n'.join(first_row_list[:]))