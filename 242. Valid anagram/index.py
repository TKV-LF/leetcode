class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp1 = {}
        temp2 = {}
        for i in range(len(s)):
            if s[i] in temp1:
                temp1[s[i]] += 1
            else:
                temp1[s[i]] = 1
            if t[i] in temp2:
                temp2[t[i]] += 1
            else:
                temp2[t[i]] = 1

        for x in temp1:

            if (x not in temp2) or (temp1[x] != temp2[x]):
                return False
        return True