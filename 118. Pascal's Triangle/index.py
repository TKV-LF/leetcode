def generate(numRows):
    if numRows == 1:
        return [[1]]
    result = [[1], [1, 1]]
    tempArr = [1]
    i = 2
    j = 0
    while i < numRows:
        if len(tempArr) == i:
            i += 1
            tempArr.append(1)
            result.append(tempArr)
            tempArr = [1]
            j = 0
        tempArr.append(result[i - 1][j] + result[i - 1][j + 1])
        j += 1

    return result

print(generate(5))