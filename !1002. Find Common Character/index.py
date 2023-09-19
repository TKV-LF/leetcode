def commonChars(words):
    result = []
    temp3 = []
    for c in words[0]:
        result.append(c)
    if len(words) == 1:
        return result
    for i in range(1, len(words)):
        temp = []
        for c in words[i]:
            temp.append(c)
        temp3 = [value for value in result if value in temp]

    return temp3


commonChars(["bella", "label", "roller"])
