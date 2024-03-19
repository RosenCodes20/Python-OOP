def lower_chars(function):

    def wrapper():
        result = function()
        return result.lower()

    return wrapper


@lower_chars
def say_hello():
    return "HELLO THERE!"


print(say_hello())