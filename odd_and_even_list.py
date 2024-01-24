# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# pseudocode

# create a function to merge both different list in the result
def odd_and_even (first_list, second_list):

# create an empty list to store the result
    result = []

# take all odd numbers on the first list
    for num in first_list:
        if (num % 2) != 0:
            result.append (num)

# taske all even number on the second list
    for num in second_list:
        if (num % 2) == 0:
            result.append (num)

# return the result of both list
    return result

# print the result
first_list = [7, 24, 59, 77, 105]
second_list = [10, 23, 49, 100, 138]

print (f"First list : {first_list}")
print (f"Second list : {second_list}")
print (f"The result is : {odd_and_even(first_list, second_list)}")