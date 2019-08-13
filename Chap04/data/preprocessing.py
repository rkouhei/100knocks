import MeCab

filename = 'neko.txt'
outputfile = 'neko.txt.mecab'

with open(filename, 'r') as f :
  mecab = MeCab.Tagger()
  result = mecab.parse(f.read())

with open(outputfile, 'w') as f :
  f.write(result)