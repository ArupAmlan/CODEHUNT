class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        count = 1
        a = 0

        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                count += 1

            else:
                a = max(a,count)
                count = 1
        a = max(a,count)
        return a