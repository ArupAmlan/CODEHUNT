class Solution:
    def maxProfit(self, p: List[int]) -> int:
        buy = p[0]
        sell = 0

        for i in range(1, len(p)):
            buy = min(buy,p[i])
            sell = max(sell,p[i]-buy)

        return sell