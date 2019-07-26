def value_format(x, y, z) :
  return str(x) + '時の' + y + 'は' + str(z)

if __name__ == "__main__":
  x = 12
  y = '気温'
  z = 22.4
  print(value_format(x,y,z))