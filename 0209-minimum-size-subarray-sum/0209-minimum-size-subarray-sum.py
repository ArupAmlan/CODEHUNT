class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        m = float('inf')
        s = 0

        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                m = min(m, r - l + 1)
                s -= nums[l]
                l += 1

        return m if m != inf else 0 