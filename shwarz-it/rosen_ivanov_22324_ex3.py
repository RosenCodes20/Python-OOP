matrix = [
    [2, 4, 6, 8, 10, 12],
    [14, 16, 18, 20, 22],
    [24, 26, 28, 30, 32],
    [34, 36, 38, 40, 42],
    [44, 46, 48, 50, 52, 54, 56, 60]
] # Example input the matrix can be way bigger!!

if not matrix:
    raise ValueError('Please enter something in the matrix!')

n_to_iterate = int(input())
matrix_length = len(matrix)

not_found = False

count = 0
first_index = 0
second_index = 0

for i in range(matrix_length):
    inner_length = len(matrix[i])
    count += 1

    if n_to_iterate in matrix[i]:
        second_index = matrix[i].index(n_to_iterate)
        first_index = i
        not_found = False
        break

    else:
        not_found = True

    # SECOND DECISION BUT IT IS SLOWER!!!!
    # for i in range(matrix_length):
    #     inner_length = len(matrix[i])
    #     count += 1
        # for j in range(inner_length):
        #     count += 1
        #     if n_to_iterate not in matrix:
        #         not_found = True
        #
        #     if matrix[i][j] == n_to_iterate:
        #         print(f'[{i}, {j}]')
        #         not_found = False
        #         break

    # if not not_found:
    #     break

if not not_found:
    print(f'[{first_index}, {second_index}]')

else:
    print('Not found!')

print(f'Number iterations: {count}')