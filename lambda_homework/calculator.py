num_one, num_two, operator = input().split()
num_one, num_two = int(num_one), int(num_two)
operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y if x > 0 and y > 0 else "Can't divide by zero",
    "*": lambda x, y: x * y
}

print(operators[operator](num_one, num_two))