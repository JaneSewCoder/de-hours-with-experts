
""" 
For a given number, return the next largest number that 
can be created by rearranging that number's digits.
1. Convert number to string.
2. Iterate through string to identify largest digit from 
  right of number. Note as index [i]
  (if largest digit is index 0, then return '-1')
3. Identify smallest digit right of index [i]. Note as index [j]
4. Convert string to array.
5. Swap i and j.
6. Sort ascending values for digits to right of [i].
7. Convert array to new string.
8. Return new number.
"""
#!/usr/bin/python3
import sys

def main():
    # next_biggest_number(sys.argv[1])




def next_biggest_number(num):
    #TODO: Implement me!
    numStr = str(num)
    print("Starting number is: ", numStr)


    #Convert input to array
    numList = [int(i) for i in numStr]

    

    #find bigger number starting from end of array 
    for i in range(len(numStr) - 1, 0, -1):
      if numStr[i] > numStr[i - 1]:
        break 

    # Return -1 if no greater number possible
    if i == 1 and numStr[i] <= numStr[i - 1]:
      print(-1)
      return -1
        
    # Identify smallest index to the left of 'bigger'
    indxPos = i

    for j in range(i + 1, len(numStr)):
      if numStr[j] > numStr[indxPos - 1] and numStr[j] < numStr[i]:
        indxPos = j
        #break

    # Swap the smaller with bigger
    numList[indxPos], numList[i-1] = numList[i-1], numList[indxPos]

    # Convert swapped list to string
    newStr = ""
    for char in numList:
        newStr += str(char)

    #Sort digits after bigger into ascending open
    digits = sorted(numList[i:])

     #Make revised list
    newNumList = numList[:i] + digits
 
  # Convert array back to string, then number
    newStr = ""
    for char in newNumList:
      newStr += str(char)
      newNewStr = int(newStr)

  # Return next greatest number
    print("Next greatest number is: ", newNewStr)
    return newNewStr
            
    # return 0


if __name__ == "__main__":
    main()

