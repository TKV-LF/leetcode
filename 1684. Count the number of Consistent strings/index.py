def countConsistentStrings(allowed, words):
    dic1 = {}
    count = 0
    for c in allowed:
        dic1[c] = 0

    for w in words:
        check = True
        for c in w:
            if c not in dic1:
                check = False
                break
        if check:
            count += 1

    return count


print(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))