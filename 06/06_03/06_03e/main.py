# use a deque as a stack 
# here were saving browser history

from collections import deque


history_stack = deque()   # create stack
history_stack.append("https://www.myspace.com")
history_stack.append("https://www.webkinz.com")
history_stack.append("https://www.cats.com")

print(history_stack[-1])      #does this without removing?
print(history_stack.pop())    # prints the top of the stack


