class Solution:
    def nextGreaterElement(self, a: List[int], b: List[int]) -> List[int]:
        stack = []
        ans = {}

        for i in reversed(b):
            while stack and stack[-1] <= i:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i)

        return [ans[i] for i in a]
            