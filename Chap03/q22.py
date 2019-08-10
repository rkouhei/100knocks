from q20 import read_uk_data
import re

content = repr(read_uk_data())
pattern = re.compile(r'\[\[Category:(.*?)[\||\]]')

result = pattern.findall(content)

for line in result :
  print(line)