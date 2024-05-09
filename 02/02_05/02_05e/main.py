seating_chart = [
    ["Sarah", "Claire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

print(seating_chart[2][1]) # this will return Laurn 

# here i am printing out the seating chart doing so by using a counter and an iterable? 
# we want the row to start at 1 not 0 so + 1
for i, row in enumerate(seating_chart):
    print(f"row {i + 1}, students {row}" ) # so we are printing out rows here 


# now we are doing seat numbers too, so we need to use a column as well
# the j index is used to access the seat. 
# since we are iterating through rows and columns we can use j to pull out the student name 
for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat {j+1}")


