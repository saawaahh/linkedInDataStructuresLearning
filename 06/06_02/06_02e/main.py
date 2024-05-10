# using stacks like a deck of cards


card_stack = []

card_stack.append("jack of hearts")
card_stack.append("2 of diamonds")
card_stack.append("10 of spades")
card_stack.append("queen of clubs")

# --- front(bottom) <-> back(top) ---

top_card = card_stack.pop()   # gives the top item in the stack bc its a stack 
print(top_card)   # here it should be miss queen club 

# to retrieve it without removing it we can use a negative index ?
# this returns 10 of spades but i did add an extra card in my example
# so i kinda think its just accessing the -1 spot lol 
top_card = card_stack[-1]
print(top_card)

# use len to find the length of a stack
if not card_stack:
  print("shes empty")

else:
  print(len(card_stack))
