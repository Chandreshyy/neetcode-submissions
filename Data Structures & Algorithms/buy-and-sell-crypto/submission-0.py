class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxx = 0
        for i in range(n):
            for j in range(i+1, n):
                cur = prices[j] - prices[i]
                maxx = max(cur, maxx)
        
        return maxx
