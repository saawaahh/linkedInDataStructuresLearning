# use a queue to print binary numbers 

from collections import deque   #import deque
# the binary numbers 
# notice its the number then a 0 inserted
# then its replaced with a 1 
# we are reading up and down not left to right 

# 1
# 10
# 11
# 100
# 101
# 110
# 111
# 1000


def print_binary_numbers(n):
  if n <= 0:
    return 
  
  queue = deque()   # created the deck
  queue.append(1)

  # print out first n binary numbers by looping over n
  for i in range(n):
    binary = queue.popleft()  # this is 1
    print(binary)
    #now were adding the 0
    #again we are looking and reading this pattern up and down not left to right
    queue.append(binary * 10)   # to get the 0 we multiply the binary by 10
    queue.append(binary * 10 + 1)   # to get a 1 we mult the binary by 10 and then add a 1


# now lets call our function
# heres a "few" calls 
print_binary_numbers(6)
print()
print_binary_numbers(-9)
print()
print_binary_numbers(0)
print()
print_binary_numbers(2)
print()
print_binary_numbers(10)
