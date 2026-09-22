class Solution:
    def maxProfit(self, p: List[int]) -> int:
        buy = float('inf')
        sell = 0

        for i in range(len(p)):
            buy = min(buy,p[i])
            sell = max(sell,p[i]-buy)

        return sell