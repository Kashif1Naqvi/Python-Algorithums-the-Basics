
items = [6,20,8,19,56,23,87,41,49,53]

def mergesort(dataset):
  if len(dataset) > 1:
    mid = len(dataset) // 2
    leftarr = dataset[:mid]
    rightarr = dataset[mid:]

    mergesort(leftarr)
    mergesort(rightarr)

    i=0
    j=0
    k=0

    while i < len(leftarr) and j < len(rightarr):
        if leftarr[i] < rightarr[j]:
          dataset[k] = leftarr[i]
          i +=1
        else:
          dataset[k] = rightarr[j]
          j+=1
        k+=1


    while  i < len(leftarr):
        dataset[k] = leftarr[i]
        i+=1
        k+=1
    while j< len(rightarr):
        dataset[k] = rightarr[j]
        j+=1
        k+=1
      

#  test with merge sort of data

print(items)
mergesort(items)
print(items)

# output
# [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
# [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]