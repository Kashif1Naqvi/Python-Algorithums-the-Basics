items = [1,2,3,4,5,6,7,8,9,11]

def find_items(item,itemslist):
  for i in range(0,len(items)):
    if item == itemslist[i]:
      return i

  return None
print(find_items(11,items)) 

# output: 9