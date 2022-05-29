class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = 0
        profit = 0
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[buy_ptr]:
                buy_ptr = i
            profit = prices[i] - prices[buy_ptr]
            max_profit = max(profit, max_profit)
        return max_profit