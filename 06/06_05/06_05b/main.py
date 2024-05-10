# matching parenthesis challenge 

from collections import deque

def check_matching_parenthsis(s):
  stack = deque()   # create deck stack
  for char in s:
    # if we see the start of a parenthesis '(' we add to stack
    if char == "(":
      stack.append(char)
    elif char == ")":   #pop off stack if its closed
      if not stack:   # in the case of it being empty
        return False
      stack.pop()

  return len(stack) == 0    # if it equals 0 the string has matching parenthesis



# lets make some calls to test this function
print(check_matching_parenthsis("()"))
print(check_matching_parenthsis("(hi there)"))
print(check_matching_parenthsis("(hell)o"))
print(check_matching_parenthsis("((linkedin)) learning"))

print(check_matching_parenthsis("(hi(there"))
print(check_matching_parenthsis("()ok)"))
print(check_matching_parenthsis("((increment)"))
print(check_matching_parenthsis(")linkedin()"))
