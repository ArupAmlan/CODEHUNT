class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # a = []
        # b = []

        # for i in nums:
        #     if i != 0:
        #         a.append(i)
        #     else:
        #         b.append(i)
        
        # nums[:] = a + b

        ans = []
        c = nums.count(0)
        for i in nums:
            if i != 0:
                ans.append(i)
        ans.extend([0]*c)
        nums[:] = ans