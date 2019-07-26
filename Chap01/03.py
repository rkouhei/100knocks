target = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
target = target.replace(',','')
target = target.replace('.','')

lis = target.split(' ')
lenlis = list(len(word) for word in lis)

print(lenlis)