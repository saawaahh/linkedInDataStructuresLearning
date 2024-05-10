# heree we are creating a set 

primary_colors = set(["blue", "red", "yellow"])


# check to see if a color is primary 
color = "pink"

if color in primary_colors:
  print(color + " be primary")
else:
  print(color + " is not primary, i fear")


# now lets create a new set 
letters = set(["a", "b"])
letters.add('c')      #add letter c to the set 
print(letters)    # this prints c, b, a => its important to notee that addind adds to the first index
