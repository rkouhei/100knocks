import urllib.parse, urllib.request
from q20 import read_uk_data
import re
import json

content = repr(read_uk_data())

pattern = re.compile(r'\|([^\s]*?)\s=(.*?)\\n')
rem_pattern = re.compile(r'(\\\'){2,5}|\[\[|\]\]|\<(.*?)\>|\[http\:(.*?)\s|\]')
results = pattern.findall(content)

res_dic = {}
for line in results :
  res_dic[line[0]] = rem_pattern.sub('', line[1])

# 国旗画像のurl取得
data = res_dic['国旗画像']
json_url = 'https://www.mediawiki.org/w/api.php?' + "action=query" + "&format=json" + "&titles=File:" + urllib.parse.quote(data) + "&prop=imageinfo" + "&iiprop=url"
with urllib.request.urlopen(json_url) as res :
  body = json.loads(res.read().decode())
  print(body['query']['pages']['-1']['imageinfo'][0]['url'])