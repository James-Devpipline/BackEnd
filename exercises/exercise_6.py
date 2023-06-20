'''
Challenge 1: Anagram Checker
Write a function is_anagram(word1, word2) that takes two strings word1 and word2 as input and returns True if the words are anagrams (contain the same letters in a different order), and False otherwise.
Example:
Input: "listen" , "silent"
Output: True
Challenge 2: List Flattening
Write a function flatten_list(lst) that takes a nested list lst as input and returns a new list that contains all the elements from the nested list in a flattened structure.
Example:
Input: [1, [2, [3, 4], 5], 6]
Output: [1, 2, 3, 4, 5, 6] 
'''

def is_anagram(word1, word2): 
    print(f'first word: {word1}')
    print(f'second word: {word2}')

    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

print(is_anagram("listen", "silent"))
print(is_anagram("test", "asdf"))

print('\n-------------------------------------------\n')

def flatten_list(lst):
    working_list = []
  
    while lst:
        item = lst.pop(0)
      
        if isinstance(item, list):
            lst = item + lst
        else:
            working_list.append(item)
    return working_list

test_list = [1, [2, [3, 4], 5], 6]

print(f'Before: {test_list}')
print(f'After: {flatten_list(test_list)}')

