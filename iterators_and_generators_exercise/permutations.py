from itertools import permutations


def possible_permutations(elements_list):
    for element in permutations(elements_list):
        yield list(element)


[print(n) for n in possible_permutations([1, 2, 3])]