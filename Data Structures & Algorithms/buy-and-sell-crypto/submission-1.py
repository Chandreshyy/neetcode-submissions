class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        minn = prices[0]
        i = 1
        while i < n:
            minn = min(minn, prices[i-1])
            cur_profit = prices[i] - minn
            profit = max(profit, cur_profit)
            i += 1
        
        return profit
