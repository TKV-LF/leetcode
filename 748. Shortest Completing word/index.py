def shortestCompletingWord(licensePlate, words):
    plate = {}
    total = 0
    for i in licensePlate:
        if (not i.isnumeric()) and i != " ":
            total += 1
            if i.lower() in plate:
                plate[i.lower()] += 1
            else:
                plate[i.lower()] = 1

    for i, value in enumerate(words):
        if len(value) < total:
            continue
        temp = plate.copy()
        for j in value:
            if j in plate and temp[j] > 0:
                temp[j] -= 1
        if sum(temp.values()) == 0:
            if result == "":
                result = value
            elif len(value) < len(result):
                result = value

    return result

print(shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))
