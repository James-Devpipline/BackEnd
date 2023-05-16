'''
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

list_3 = [54, 44, 27, 79, 91, 41]

def swap_two_and_four(list):
    remove_index_four = list.pop(4)
    remove_index_two = list.pop(2)
    list.insert(2, remove_index_four)
    list.insert(4, remove_index_two)

    print(list)

swap_two_and_four(list_3)