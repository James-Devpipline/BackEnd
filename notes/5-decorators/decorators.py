import functools


def my_decorator(func):
    @functools.wraps(func)
    def decorator_wrapper(*args, **kwargs):
        # some code goes here to do your magic things
        new_message = f"{args[0].upper()}!!!!!!!!!!!!"
        args = [new_message]
        return func(*args, **kwargs)

    return decorator_wrapper
