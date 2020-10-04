def create_matrix(matrix_size: int):
    # matrix = [['X' if i == index else '_' for i in range(matrix_size)] for index in range(matrix_size)]
    matrix = []
    for index in range(matrix_size):
        matrix.append(['X' if i == index else '_' for i in range(matrix_size)])
    return matrix


matrix = create_matrix(3)
for line in matrix:
    for index, matrix_element in enumerate(line):
        if index == len(line) - 1:
            print(matrix_element)
        else:
            print(matrix_element, end=' ')
