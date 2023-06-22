"""
Given two Python lists, write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
Given:
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:
10 400

20 300

30 200

40 100
"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

def transverse_and_reverse(listToBeInOrder, listToBeInReverse):
    for i in range(1, len(listToBeInOrder)+1):
        print(f'{listToBeInOrder[i-1]} {listToBeInReverse[-i]}')


transverse_and_reverse(list1, list2)