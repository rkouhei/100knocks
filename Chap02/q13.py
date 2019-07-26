path1 = 'data/col1.txt'
path2 = 'data/col2.txt'
path3 = 'data/col3.txt'

col1 = open(path1, 'r')
col2 = open(path2, 'r')
col3 = open(path3, 'w')

lines1 = col1.readlines()
lines2 = col2.readlines()

for line1, line2 in zip(lines1, lines2) :
  line1 = line1.replace('\n', '\t')
  tmp = line1 + line2
  col3.write(tmp)

col1.close()
col2.close()
col3.close()