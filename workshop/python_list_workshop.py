import sys
from collections import deque


class List:
    def __init__(self, my_list: list):
        self.my_list = my_list

    @property
    def my_list(self):
        return self.__my_list

    @my_list.setter
    def my_list(self, value):
        if type(value) not in [list, deque]:
            raise ValueError("You can only start with list!!!")

        if not value:
            raise ValueError("The list cannot be empty!!")

        self.__my_list = value

    def append(self, value):
        self.my_list.append(value)
        return self.my_list

    def remove(self, index):
        if index not in self.my_list:
            raise Exception("Element is not in our list!!")

        return self.my_list.remove(index)

    def get(self, index):
        if not 0 <= index < len(self.my_list):
            raise IndexError("Invalid index!!!")

        return self.my_list[index]

    def extend(self, iterable):
        if type(iterable) not in [list, dict, tuple, set]:
            raise ValueError("Not right Value!!!!")

        self.my_list.extend(iterable)
        return self.my_list

    def insert(self, index, value):
        if not 0 <= index < len(self.my_list):
            raise IndexError("Index not in right diapason!")

        self.my_list.insert(index, value)
        return self.my_list

    def pop(self):
        return self.my_list.pop()

    def clear(self):
        self.my_list.clear()
        return self.my_list

    def index(self, value):
        index = 0
        if value not in self.my_list:
            raise ValueError("Value is not in the list!")

        for element in self.my_list:
            if element != value:
               index += 1

            elif element == value:
                return index

    def count(self, value):
        count = 0
        if value not in self.my_list:
            raise ValueError("Value not in the list!")

        for element in self.my_list:
            if element == value:
                count += 1

        return count

    def reverse(self):
        return self.my_list.reverse()

    def copy(self):
        return self.my_list.copy()

    def sort(self):
        return self.my_list.sort()

    def size(self):
        length = len(self.my_list)
        return length

    def add_first(self, value):
        if not isinstance(value, int):
            raise ValueError("Our list is formed only by integers!")

        self.my_list = deque(self.my_list)
        self.my_list.appendleft(value)
        self.my_list = list(self.my_list)
        return self.my_list

    def dictionize(self):
        list_dict = {}
        while True:
            if not self.my_list:
                break

            even_value = self.my_list.pop(0)

            if self.my_list:
                odd_values = self.my_list.pop(0)

            else:
                odd_values = " "

            if even_value not in list_dict:
                list_dict[even_value] = odd_values

        return list_dict

    def move(self, amount):
        if not 0 <= amount < len(self.my_list):
            raise ValueError("Please enter a valid amount of numbers")

        amount_to_add = self.my_list[:amount]
        self.my_list.extend(amount_to_add)
        self.my_list[:amount] = ""
        return self.my_list

    def sum(self):
        list_sum = 0
        for element in self.my_list:
            if isinstance(element, int):
                list_sum += element

            elif isinstance(element, str):
                list_sum += len(element)

        return list_sum

    def overbound(self):
        max_length_of_value = -sys.maxsize
        for element in self.my_list:
            if isinstance(element, int):
                if element > max_length_of_value:
                    max_length_of_value = element

            elif isinstance(element, str):
                if len(element) > max_length_of_value:
                    max_length_of_value = len(element)

        return max_length_of_value

    def underbound(self):
        lowest_num_length = sys.maxsize

        for element in self.my_list:
            if isinstance(element, int):
                if element < lowest_num_length:
                    lowest_num_length = element

            elif isinstance(element, str):
                if len(element) < lowest_num_length:
                    lowest_num_length = len(element)

        return lowest_num_length

