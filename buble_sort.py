# Buble Sorting program

def bubbleSort(dataset):
  for i in range(len(dataset)-1 , 0 , -1):
    for j in range(i):
      if(dataset[j]> dataset[j+1]):
        temp = dataset[j]
        dataset[j] = dataset[j+1]
        dataset[j+1] = temp
          
  print("Current  State is:",dataset)

def main():
  list = [1,4,57,5,12,54,524,542,45,2,45,452,452,4,1521,1,2,15,45,45,7,5,19,31,31,94,6341]
  bubbleSort(list)
  print("Result:",list)

if __name__ == "__main__":
    main()