class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            while need in seen:
                return [i,seen[need]]
            seen[nums[i]] = i
        return seen