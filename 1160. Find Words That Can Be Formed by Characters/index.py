def countCharacters(words, chars):
    dict1 = {}
    result = 0

    for c in chars:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1
    for w in words:
        tempDict = dict1.copy()
        check = True
        for c in w:
            if c not in tempDict:
                check = False
                break
            tempDict[c] -= 1
            if tempDict[c] < 0:
                check = False
                break
        if check:
            result += len(w)

    return result


print(countCharacters(["cat", "bt", "hat", "tree"], "atach"))
