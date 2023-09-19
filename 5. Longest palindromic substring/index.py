class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        max = ''
        for i, char in enumerate(s):
            left = self.helper(i, i, s)
            right = self.helper(i, i+1, s)
            curr = left if len(left) >= len(right) else right
            max = curr if len(curr) > len(max) else max
        return max

    def helper(self, left, right, s):
        curr = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr = s[left:right+1]
            left -= 1
            right += 1
        return curr

