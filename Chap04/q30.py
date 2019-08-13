def read_data():
  filename = './data/neko.txt.mecab'
  result = []
  tmp = []
  with open(filename, 'r') as content :
    for line in content :
      line = line.split('\t')
      if len(line) == 1 :
        return result
      des = line[1].split(',')
      dic = {
        'surface': line[0],
        'base': des[6],
        'pos': des[0],
        'pos1': des[1]
      }
      tmp.append(dic)
      if(line[0] == '。') :
        result.append(tmp)
        tmp = [] # tmpを空に

if __name__ == "__main__":
  res = read_data()
  print(res[0:5])