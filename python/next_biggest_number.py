#first commit 2/24/21 19:54

#!/usr/bin/python3
#import sys

def main():
    # next_biggest_number(sys.argv[1])
    next_biggest_number(543621)


def next_biggest_number(num):
    #TODO: Implement me!
    #numStr = str(num)

    #Convert input to array
    numList = [int(i) for i in str(num)]
    
    print(numList, "initial array")
    
    # print(numStr)
    # print(len(numStr))
    
    #find smallest number starting from end of array 
    for i in range(len(str(num)) - 1, 0, -1):
      biggest = 0
      #print(i)
      if numList[i] > numList[i - 1]:
        biggest = numList[i]
        # bigIndx = i
        print(biggest, " is the first biggest digit")
        break
      # else:
      #   print(-1)

    # return -1 if no greater number possible
    if i == 1 and numList[i] <= numList[i - 1]:
      print(-1)
      return
        
    # Identify smallest digit to the right of 'bigger'
    biggerIndx = numList[i - 1]
    indxPos = i
    # print("Digit # ", bigger, " has an index of: ", indxPos)
        # print(i)
    for j in range(i + 1, len(str(num))):
      # print("index is: ", j, "digit is: ", numList[j])
      if numList[j] > biggerIndx and numList[j] < numList[indxPos]:
        indxPos = j
        print("value at J ", numList[indxPos])
      # else:
      #   print("else")
        
    # Swap the smaller with bigger
    numList[indxPos], biggerIndx = biggerIndx, numList[indxPos]

    #print(numList)

    result = 0
    for j in range(i):
      result = result * 10 + numList[j]
      print(result)
    print(numList, "after swap")
      
    #Sort digits after bigger into ascending open
    digits = sorted(numList[i:])
    print(digits, " sorted")

    for j in range(len(str(num)) - 1):
      result = result * 10 + numList[j]

    print("Next greatest number is: ", result)







            
    # return 0



if __name__ == "__main__":
    main()

