def countWords(words1, words2):
    dict1, dict2 = {}, {}
    count = 0
    for i in words1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in words2:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    for i in dict1:
        if i in dict2 and dict1[i] == 1 and dict2[i] == 1:
            count += 1
    return count
