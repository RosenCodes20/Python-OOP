def even_numbers(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [r for r in result if r % 2 == 0]
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
