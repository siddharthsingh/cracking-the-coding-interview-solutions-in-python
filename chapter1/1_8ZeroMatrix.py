def zeroMatrix(matrix):
    if not matrix:return []
    zero_pos_row = []
    zero_pos_col = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j in zero_pos_col:
                continue
            elif matrix[i][j] == 0:
                zero_pos_col.append(j)
                zero_pos_row.append(i)


    for i in zero_pos_row:
        matrix[i] = [0]*len(matrix[0])

    for j in zero_pos_col:
        for i in range(len(matrix)):
            matrix[i][j] = 0
    return matrix

matrix = [[1, 0, 0, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(zeroMatrix(matrix))
