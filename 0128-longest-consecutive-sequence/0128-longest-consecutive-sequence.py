class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        count = 1
        ls = 0

        for i in range(len(nums)- 1):
            if nums[i] + 1 == nums[i+1]:
                count += 1

            else:
                ls = max(ls,count)
                count = 1

        ls = max(ls,count)
        return ls