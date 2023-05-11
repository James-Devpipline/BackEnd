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
Exercise 2: Swap two list elements
Write a program to swap elements 2 and 4 in a given list:
Input:
list_1 = [54, 44, 27, 79, 91, 41]
Expected Output:
List before swapping elements:
[54, 44, 27, 79, 91, 41]

List after swapping elements 2 and 4:
[54, 44, 91, 79, 27, 41]
'''

## exercise 1

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

## exercise 2
list_3 = [54, 44, 27, 79, 91, 41]

def swap_two_and_four(list):
    remove_index_four = list.pop(4)
    remove_index_two = list.pop(2)
    list.insert(2, remove_index_four)
    list.insert(4, remove_index_two)

    print(list)

swap_two_and_four(list_3)