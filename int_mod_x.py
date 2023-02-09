# gcd(num1, num2) computes the greatest common divisor
#  of num1 and num2. 
# time: O(n)
def get_gcd(num1, num2):
  if num1 == 0:
    return num2
  elif num2 == 0:
    return num1
  else:
    remainder = num1 % num2
    while remainder:
      num1 = num2
      num2 = remainder
      remainder = num1 % num2
  return num2

# int_mod_x(n) determines the elements that contain
#   multiplicative inverses in (Zn)^x
# time: O(n^2)
def int_mod_x(n):
  lon = []
  for i in range(n):
    if get_gcd(i, n) == 1:
      lon.append(i)
  return lon

def generator(a, n, mod):
  lon = []
  flag = 0
  for i in range(1, n + 1):
    if flag == 1:
      break
    n = (a**i) % mod
    if (n == 1):
      flag = 1
    lon.append(n)
  return lon


lon = generator(17, 43, 98)
lst = generator(11, 42, 98)
print(len(lst))

print(lon)
print(lst)
print(lst == lon)

