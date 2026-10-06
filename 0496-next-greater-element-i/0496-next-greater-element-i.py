class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums2)
        ans = [-1] * n
        stack = []

        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            else:
                ans[i] = -1
            stack.append(nums2[i])

        return [ans[nums2.index(i)] for i in nums1]