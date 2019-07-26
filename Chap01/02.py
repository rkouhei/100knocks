target1 = 'パトカー'
target2 = 'タクシー'
ans = ''

for i,j in zip(target1, target2) :
    ans += (i+j)
print(ans)