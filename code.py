def gcd(a,b):
  while(b !=0):
    t = a
    a = b
    b = t % b
    return b 
print(gcd(44,3))
print(gcd(44,44))
# output:
# 2
# 0