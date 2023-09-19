from string import ascii_lowercase as alc


def checkDistances(s, distance):
    dict1 = {}
    alpha = {}
    for i, value in enumerate(s):
        if value in dict1:
            dict1[value] = i - dict1[value] - 1
        else:
            dict1[value] = i
    for i in range(26):
        alpha[alc[i]] = distance[i]
    for i in dict1:
        if i in alpha:
            if dict1[i] != alpha[i]:
                return False
	
    return True
