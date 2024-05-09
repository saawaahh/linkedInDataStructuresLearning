''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

ITEM_AT_INDEX_3 = student_pet_count_list[3] # should be 2
ITEM_THREE_FROM_BACK = student_pet_count_list[-3] # should be 2 


student_pet_count_list[2] = 3   # here we are updating/ "mutating" the list
student_pet_count_list[3] = student_pet_count_list[3] + 1   # say this student got a new pet, its best to then add one this way instead of overriding it 
student_pet_count_list[-1] = student_pet_count_list[-1] + 2

# say you got a new student mid year and you want to add them to the list
# you do this using append 
student_pet_count_list.append(4)

# this needs to be moved down here bc we need to calculate students considering our new besites
NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)

SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:         #created individual pet count in the for loop
  SUM = SUM + INDIVIDUAL_PET_COUNT
print(SUM)


# calculate the average number of pets in the class
AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)


