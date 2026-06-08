class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, profit = 0, 0

        if prices is None:
            return profit

        for R in range(1, len(prices)):
            curProfit = prices[R] - prices[L]
            if curProfit < 0:
                L = R 
            profit = max(profit, curProfit)

        return profit 


        