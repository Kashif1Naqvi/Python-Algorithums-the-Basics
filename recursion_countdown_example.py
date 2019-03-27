# let start to build counter for countdown

def countdown(x):
  if(x==0):
    print("Done!")
    return
  else:
    print(x,"....")
    countdown(x-1)

countdown(5)

# output:
# 5 ....
# 4 ....
# 3 ....
# 2 ....
# 1 ....
# Done!
