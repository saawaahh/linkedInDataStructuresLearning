# we are doing union, intersection, ect


set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

# this leaves the initial sets unbothered and creates a new set with both
union_set = set_A.union(set_B)
print(union_set)

# this creates a new set with items that are in both
# so in this example it will only be: 30, 40, 50
intersection_set = set_A.intersection(set_B)
print(intersection_set)

# this will print what is in set A that is not in set B
# so in this example 10 and 20
difference_set = set_A.difference(set_B)
print(difference_set)

# print what is in set B that is not in set A
# here it is 70 and 60
difference_set_BA = set_B.difference(set_A)
print(difference_set_BA)

# print whats in the sets but not in both sets
# here it is 10, 20, 60, 70
symmetric_difference_set = set_A.symmetric_difference(set_B)
print(symmetric_difference_set)
