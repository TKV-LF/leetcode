class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        for i in range(len(nums)):
            if nums[i] in list:
                return [list[nums[i]], i]
            list[target-nums[i]] = i