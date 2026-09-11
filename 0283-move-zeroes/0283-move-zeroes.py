class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #approach - 1

        # a = []
        # b = []

        # for i in nums:
        #     if i != 0:
        #         a.append(i)
        #     else:
        #         b.append(i)
        
        # nums[:] = a + b

        #approach - 2

        # ans = []
        # c = nums.count(0)
        # for i in nums:
        #     if i != 0:
        #         ans.append(i)
        # ans.extend([0]*c)
        # nums[:] = ans

        #approach - 3

        l = 0 

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1

            