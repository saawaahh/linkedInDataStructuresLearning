# making an immutable/frozen sett

primary_colors = frozenset(["red", "blue", "yellow"])       # primary colors do not change so it makes sense to make it a frozen set

if "blue" in primary_colors:
    print("Blue in the set!")

# primary_colors.add("green"). # this will throw an error bc its not in the set and the set cannot be changed so it cant be added
