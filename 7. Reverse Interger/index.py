class Solution:
    def reverse(self, x: int) -> int:
        reverseNumber = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            remainder = x % 10
            if (reverseNumber > (2**31 - 1) / 10) or ((reverseNumber == (2**31 - 1) / 10) and (remainder > 7)):
                return 0
            if (reverseNumber < (-2**31) / 10) or ((reverseNumber == (-2**31) / 10) and (remainder < -8)):
                return 0
            reverseNumber = reverseNumber * 10 + remainder
            x = x // 10
        return sign * reverseNumber
