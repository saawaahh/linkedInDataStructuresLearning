# i am supposed to find the second smallest number in the list

# timesort? n log n 
def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None             # here is returns none if the its empty, but idk why its < 2 maybe bc second big? idkk 
    sorted_list = sorted(my_list)
    return sorted_list[1]


# second option is to create a custom algorithm 
# here we are going to iterate through the list keeping track of the two smallest items
# O(n) bc we only iterate through the list once
def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    
    smallest = float('inf')
    second_smallest = float('inf')          # i guess here we are making it big knowing that we will be overriding as we go 

    for num in my_list: 
        if num < smallest:
            second_smallest = smallest
            smallest = num              # oh okay i see lol 
        elif num < second_smallest:
            second_smallest = num
    return second_smallest


print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))


