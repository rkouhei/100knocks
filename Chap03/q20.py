import json, gzip
path = 'data/jawiki-country.json.gz'

def read_uk_data() :
  with gzip.open(path, mode='rt') as fp :
    for line in fp :
      data = json.loads(line)
      if data['title'] == 'イギリス' :
        # print(data['text'])
        return data['text']
  
  raise ValueError('なし')

if __name__ == "__main__":
  print(read_uk_data())