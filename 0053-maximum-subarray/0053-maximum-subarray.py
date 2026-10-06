class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = maximum = nums[0]

        for i in nums[1:]:
            current = max(i, current + i)
            maximum = max(current, maximum)

        return maximum