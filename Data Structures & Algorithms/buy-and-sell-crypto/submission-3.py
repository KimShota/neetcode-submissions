class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        left = 0 
        right = 1 
        n = len(prices)

        while right != n:
            result = max(result, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right 
                right += 1 
            else:
                right += 1 
        
        return result 
