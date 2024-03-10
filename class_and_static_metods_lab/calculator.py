class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def subtract(*args):
        element = args[0]

        for elements in args[1:]:
            element -= elements

        return element

    @staticmethod
    def multiply(*args):
        element = args[0]

        for elements in args[1:]:
            element *= elements

        return element

    @staticmethod
    def divide(*args):
        element = args[0]

        for elements in args[1:]:
            element /= elements

        return element


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
