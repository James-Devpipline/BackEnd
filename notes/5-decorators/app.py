'''
Functions:
Codeblock - send and recieve info
takes parameters

Set of instructions

Helps us keep our code DRY

a = 7

def function_name(a, b, c, x = None)
    a = 5
    b = 5
    c = 5

Arguments > Locally Scoped
Position, Keyword

Pass by Value vs Pass by Reference
    Passing by value means that when you give a variable to a function, it creates a copy of that variable inside the function. Any changes made to the copy won't affect the original variable outside of the function.

    Passing by reference means that instead of creating a copy, the function receives a direct link or reference to the variable. Any changes made to the variable inside the function will affect the original variable outside of the function.
'''


# from decorators import my_decorator


# def my_func(lst):
#     return lst.sort()


# my_list = [1, 4, 5, 2, 8, 10, 3, -43]

# #######
# # PASS BY VALUE (passing in a value)
# print(my_list)  # returns 1, 4, 5, 2, 8, 10, 3, -43]
# new_lst = my_func(my_list)
# print(new_lst)  # returns [-43, 1, 2, 3, 4, 5, 8, 10]
# print(my_list)  # returns 1, 4, 5, 2, 8, 10, 3, -43]

# #######
# # PASS BY REFERENCE (passing in the reference of the variable (value) which then returns the same value but mutated)
# print(my_list)  # returns 1, 4, 5, 2, 8, 10, 3, -43]
# my_func(my_list)
# print(my_list)  # returns [-43, 1, 2, 3, 4, 5, 8, 10]


# @my_decorator
# def say_hello(message):
#     return message


# print(say_hello("hello"))
##########################
# my_original_value = [8]


# def my_function(a):
#     a.append(5)
#     return a
#     # returns a reference to my_original_value, not returning a


# my_new_val = my_function(my_original_value)

# print(my_original_value is my_new_val)  # returns true because my new val is

# my_new_val.append(9)

# print(my_original_value)  # prints out my_new_val with the 9 due to pass by reference
##########################

from decorators import my_decorator
from decorators import my_decorator2


@my_decorator
def say_hello(message, message_kwarg):
    return f'{message}\n{message_kwarg}'


@my_decorator2
def say_hello2(message):
    return message


print(say_hello)  # this returns its place in memory I believe
print(say_hello("hello", message_kwarg="hello from kwargs"))


print(say_hello2([1, 2, 3, 4, '5']))
