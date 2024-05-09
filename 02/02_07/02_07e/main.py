# Linear Search / sequential search
# I guess this is inelegant and a brute force method 
# this could take a long long time in the worst case 
# O(n)
# probably only really want to do for unsorted data


my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7

def search(item, listy):
    for element in listy:   # here we are searching the list sequentially
        if element == item:
            return True
    return False

print(search(ITEM, my_list))

ITEM_INDEX = my_list.index(ITEM) # index can be used to find each item in the list
