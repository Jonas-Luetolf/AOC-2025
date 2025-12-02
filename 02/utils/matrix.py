def invert(matrix: list[list]) -> list[list]:
    inv_matrix = []

    for line in matrix:
        inv_matrix.append(line[::-1])

    return inv_matrix


def transpose(matrix: list[list]) -> list:
    transposed_matrix = []

    for i in range(len(matrix[0])):
        transposed_matrix.append([line[i] for line in matrix])

    return transposed_matrix


def rotate_45(matrix):
    n = len(matrix)
    m = len(matrix[0])

    rotated_matrix = [[]]

    for i in range(n):
        for j in range(i + 1):
            rotated_matrix[-1].append(matrix[i - j][j])

        rotated_matrix.append([])

    for i in range(1, n):

        for j in range(m - 1, i - 1, -1):
            rotated_matrix[-1].append(matrix[i + (m - j - 1)][j])

        rotated_matrix[-1] = rotated_matrix[-1][::-1]
        rotated_matrix.append([])

    return rotated_matrix[:-1]
