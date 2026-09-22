class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        window = ans/k

        for i in range(k,len(nums)):
            ans = ans + nums[i] - nums[i-k]
            window = max(window,ans/k)

        return window
