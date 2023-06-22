'''
Concatenate two lists index-wise
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index element, and so on till the last element. Any leftover items will get added at the end of the new list.
Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Expected output:
['My', 'name', 'is', 'Kelly']
'''

list1 = ["M", "na", "i", "Ke", ";alksjdf"]
list2 = ["y", "me", "s", "lly"]
output = []

def concat_lists(first, second):
    # for i in min(len(first), len(second)): ####doesn't work because max and min isn't iterable with the len of both params
    max_len = max(len(first), len(second))

    for i in range(max_len):
            try:
                  output.append(first[i]+second[i])
            except:
                    try:
                          output.append(first[i])
                    
                    except:
                          output.append(second[i])
    print(output)

    
concat_lists(list1,list2)