def vowel_filter(function):
    def wrapper():
        result = function()
        return [r for r in result if r in "aeyoui"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
