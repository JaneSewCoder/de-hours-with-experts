
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
    next_biggest_number(sys.argv[1])




def next_biggest_number(num):
    #TODO: Implement me!
    num_str = str(num)
    print("Starting number is: ", num_str)


    #Convert input to array
    num_list = [int(i) for i in num_str]

    

    #find bigger number starting from end of array 
    for i in range(len(num_str) - 1, 0, -1):
      if num_str[i] > num_str[i - 1]:
        break 

    # Return -1 if no greater number possible
    if i == 1 and num_str[i] <= num_str[i - 1]:
      print(-1)
      return -1
        
    # Identify smallest index to the left of 'bigger'
    indx_pos = i

    for j in range(i + 1, len(num_str)):
      if num_str[j] > num_str[indx_pos - 1] and num_str[j] < num_str[i]:
        indx_pos = j
        #break

    # Swap the smaller with bigger
    num_list[indx_pos], num_list[i-1] = num_list[i-1], num_list[indx_pos]

    # Convert swapped list to string
    new_str = ""
    for char in num_list:
        new_str += str(char)

    #Sort digits after bigger into ascending open
    digits = sorted(num_list[i:])

     #Make revised list
    new_num_list = num_list[:i] + digits
 
  # Convert array back to string, then number
    new_str = ""
    for char in new_num_list:
      new_str += str(char)
      new_new_str = int(new_str)

  # Return next greatest number
    print("Next greatest number is: ", new_new_str)
    return new_new_str
            
    # return 0


if __name__ == "__main__":
    main()

