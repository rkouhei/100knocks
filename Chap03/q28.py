from q20 import read_uk_data
import re
import pprint

content = repr(read_uk_data())

pattern = re.compile(r'\|([^\s]*?)\s=(.*?)\\n')
rem_pattern = re.compile(r'(\\\'){2,5}|\[\[|\]\]|\<(.*?)\>|\[http\:(.*?)\s|\]')
results = pattern.findall(content)

res_dic = {}
for line in results :
  res_dic[line[0]] = rem_pattern.sub('', line[1])

pprint.pprint(res_dic)