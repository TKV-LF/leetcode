class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        temp = 0
        if (digits[len(digits) - 1] + 1) > 9:
            temp = 1
            result.append(0)
            if len(digits) == 1:
                result.insert(0, 1)
        else:
            result.append(digits[len(digits) - 1] + 1)
        for i in range(len(digits) - 2, -1, -1):
            if temp != 0:
                if (digits[i] + temp) > 9:
                    temp = 1
                    result.insert(0, 0)
                    if i == 0:
                        result.insert(0, 1)

                else:
                    result.insert(0, digits[i] + temp)
                    temp = 0
            else:
                result.insert(0, digits[i])

        return result

"""
	Short solution, but not the best
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i]*10**(len(digits)-1-i)
        num+=1
        ans = []
        for i in str(num):
            ans.append(int(i))
            
        return ans