# here we are gone sort a structure 

my_list = [1, 7, 3]
print(sorted(my_list))
print(sorted(my_list, reverse=True)) # print in the opposite order

# now lets work with tuples 
student_grades = [('Sarah', 89), ('Reb', 82), ('Matt', 91)]
print(sorted(student_grades)) # this sorts the first element, here the name, and it sorted in alphebetical order

# sort uses the natural order of how things are to be sorted starting at the first element
# to bypass this with a specific sort in mind you use a lambda function
print(sorted(student_grades, key=lambda x:x[1], reverse=True)) # here our lambda function is looking at the second element and ordering by grades 

