class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        With 2 pointers, left and right, which one have small value will be moved to the middle.
        """
        left = 0
        right = len(height) - 1
        max = 0
        while left != right:
            if max < (min(height[left], height[right]) * abs(left-right)):
                max = min(height[left], height[right]) * abs(left-right)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max
