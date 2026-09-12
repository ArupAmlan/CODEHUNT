class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        m = float('inf')

        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                m = min(m,r-l+1)
                s -= nums[l]
                l += 1
                
        return m if m!= inf else 0