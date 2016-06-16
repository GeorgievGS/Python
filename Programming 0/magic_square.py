def sum_first_diag(matrix):

    result = 0
    index = 0
    

    for row in matrix:
        result += matrix[index][index]

        index += 1

    return result

def sum_second_diag(matrix):

    result = 0
    index_row = 0
    index_column = len(matrix[0]) - 1

    for row in matrix:
        result += matrix[index_row][index_column]

        index_row += 1
        index_column -= 1

    return result

def sum_row(matrix, index):
    return sum(matrix[index])

def sum_column(matrix, index):

    result = 0

    for row in matrix:
        result += row[index]

    return result


def magic_square(matrix):

    target_sum = sum_first_diag(matrix)

    if sum_second_diag(matrix) is not target_sum:
        return False

    for index in range(0, len(matrix)):
        if sum_row(matrix, index) is not target_sum:
            return False

    for index in range(0, len(matrix[0])):
        if sum_column(matrix, index) is not target_sum:
            return False
    
    return True


square1 = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]

print(square1)
print(magic_square(square1))

    


        
