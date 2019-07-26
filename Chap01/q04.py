target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
target = target.replace(',','')
target = target.replace('.','')
word_list = target.split(' ')

initial_list = [1,5,6,7,8,9,15,16,19]
ans_dict = {}
for i in range(len(word_list)) :
  if i+1 in initial_list :
    ans_dict[i] = word_list[i][0]
  else :
    ans_dict[i] = word_list[i][0:2]

print(ans_dict)