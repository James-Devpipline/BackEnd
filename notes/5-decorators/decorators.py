import functools

# Decorators are functions that take in functions as their perameter and then expand on those functions or add functionalityß


def my_decorator(func):
    @functools.wraps(func)
    def decorator_wrapper(*args, **kwargs):  # * is like the spread operator in javascript. This gives a tuple of info of the spread out first perameter. ** changes it to a dictionary instead of a tuple. The argument name is the key and the passed in value is the value
        # some code goes here to do your magic things
        print(args)
        new_message = f"{args[0].upper()}!!!!!!!!!!!!"
        args = [new_message]  # due to tuples being immutable you have to destroy and replace args

        print(kwargs)  # returns empty if no kwargs are passed in
        kwargs['message_kwarg'] = f"{kwargs['message_kwarg'].upper()}!!!!!!!!!!!!"
        return func(*args, **kwargs)

    return decorator_wrapper


# def function_name(a, b, c, d, e, f):

#     pass


# function_name(1, 2, 3, x=5, b=22)  # manually specified perams are the keyword arguments
