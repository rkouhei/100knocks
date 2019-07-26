from q05 import n_gram

target1 = 'paraparaparadise'
target2 = 'paragraph'

X = n_gram(target1,2)
Y = n_gram(target2,2)

X_set = set(X)
Y_set = set(Y)

# print(X_set)
# print(Y_set)

# 和集合
print('和集合 : ', X_set|Y_set)

# 積集合
print('積集合 : ', X_set&Y_set)

# 差集合
print('差集合(X-Y) : ', X_set-Y_set) # Xに含まれているが、Yに含まれていないもの
print('差集合(Y-X) : ', Y_set-X_set) # Yに含まれているが、Xに含まれていないもの

# 'se'がXおよびYに含まれるか
print('seがXに含まれるか :', "se" in X_set)
print('seがYに含まれるか :', "se" in X_set)