def matrix_sum(a_matrix):
    result = []
    for elem in a_matrix:
        result += elem
    result = sum(result)
    return result


m1 = [[2, 9, 1], [3, 1, 18], [22, 8, 16]]
m2 = [[81, 29], [31, 57]]

print(matrix_sum(m1))