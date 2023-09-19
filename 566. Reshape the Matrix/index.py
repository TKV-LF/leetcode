def matrixReshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])

    if m * n != r * c:
        return mat

    count = 0
    result = []
    row = []
    for i in range(m):
        for j in range(n):
            row.append(mat[i][j])
            count += 1
            if count == c:
                result.append(row)
                row = []
                count = 0
    return result


matrixReshape([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
              [13, 14, 15, 16], [17, 18, 19, 20]], 42, 5)
