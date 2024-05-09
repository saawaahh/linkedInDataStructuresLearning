# Tuples are immutable array-like structures
# Tuples cannot be changed 

point = (5, 2)

y = point[0]
x = point[1]


# tuples can also be used to retun multiple values 
# here lets use that concept to calculate the area and perimeter of a squaree
def calculate_square_properties(side_length):
  area = side_length * side_length
  perimeter = 4 * side_length

  return(area, perimeter) # here we use a tuple to return both 


# lets build on that more
result = calculate_square_properties(5) # lets use an example of a square side length 5
print("Area: ", result[0])
print("Perimeter: ", result[1])





