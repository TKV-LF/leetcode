class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
			first sort
            use two pointers to find the rest two numbers
            if the sum is less than 0, move the left pointer to the right
            if the sum is greater than 0, move the right pointer to the left
            if the sum is 0, add the result to the list
            if the sum is 0, move the left pointer to the right and the right pointer to the left
            if the left pointer is the same as the previous one, move it to the right
            if the right pointer is the same as the previous one, move it to the left
            if the left pointer is greater than the right pointer, break the loop
            
            Space complexity: O(1)
            
            
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
