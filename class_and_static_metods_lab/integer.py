class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(value)):
            if i != 0 and roman_nums[value[i]] > roman_nums[value[i - 1]]:
                num += roman_nums[value[i]] - 2 * roman_nums[value[i - 1]]

            else:
                num += roman_nums[value[i]]

        return cls(num)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))


integer = Integer.from_string("10")
print(integer.value, 10)
