'''
Exercise 1: Custom List Merge
Given two lists, list_1 and list_2, write a program to create a third list by selecting odd-index elements from the list list_1and even index elements from the list list_2.
Given:
list_1 = [3, 6, 9, 12, 15, 18, 21]
list_2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]


Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
'''

list_1 = [3, 6, 9, 12, 15, 18, 21]
list_2 = [4, 8, 12, 16, 20, 24, 28]

def even_and_odd_list_function(list_odd, list_even):
    working_list = []

    for i in list_1:
        if list_even.index(i) % 2 != 0:
            working_list.append(i)

    for i in list_2:
        if list_odd.index(i) % 2 == 0:
            working_list.append(i)
    
    return(working_list)

print(even_and_odd_list_function(list_2, list_1))

