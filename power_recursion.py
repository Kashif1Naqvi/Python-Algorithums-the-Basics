
def power(num,pwr): 
  if(pwr==0):
    return 1
  else:
    return num * power(num,pwr-1)
print("{} and {} is  {}".format(2,6,power(2,6)))
print("{} and {} is  {}".format(6,6,power(6,6)))print("{} and {} is  {}".format(6,6,power(6,6)))

def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num-1)
print("{}! is {}".format(1,factorial(4)))
print("{}! is {}".format(5,factorial(5)))