class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count = 0
        ps = 0

        for i in range(len(nums)):
            ps += nums[i]
            if ps - k in seen:
                count += seen[ps-k]
            seen[ps] = seen.get(ps,0) + 1

        return count