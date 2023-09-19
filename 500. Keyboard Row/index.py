def findWords(words):
    row1 = dict((el, 0) for el in "qwertyuiop")
    row2 = dict((el, 0) for el in "asdfghjkl")
    row3 = dict((el, 0) for el in "zxcvbnm")
    temp = {}
    result = []
    for i in range(len(words)):
        for j in words[i]:
            if j.lower() in row1:
                temp['row1'] = 0
            if j.lower() in row2:
                temp['row2'] = 0
            if j.lower() in row3:
                temp['row3'] = 0

        if len(temp) <= 1:
            result.append(words[i])
        temp = {}

    return result


print(findWords(["Az"]))