class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = {}

        for i,j in enumerate(nums):
            need = target - j
            if need in b:
                return [b[need],i]

            b[j] = i