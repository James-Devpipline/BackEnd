'''
Exercise 3: Slice and reverse list
Write a program to slice a list into 3 equals chunks and reverse each new list
Given:
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

Expected Outcome:
Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
'''

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

def reverse_list(list):
    needed_length = len(list) / 3
    print(needed_length)
    chunk_1 = list[slice(0, int(needed_length))]
    chunk_2 = list[slice(int(needed_length), int(needed_length*2))]
    chunk_3 = list[slice(int(needed_length*2), int(needed_length*needed_length))]
    print('-----BEFORE REVERSE-----')
    print(chunk_1)
    print(chunk_2)
    print(chunk_3)
    
    chunk_1.reverse()
    chunk_2.reverse()
    chunk_3.reverse()
    
    print('-----AFTER REVERSE-----')
    print(chunk_1)
    print(chunk_2)
    print(chunk_3)

reverse_list(sample_list)
