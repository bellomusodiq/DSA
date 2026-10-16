from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = max_profit = 0
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[right] < prices[left]:
                left = right
                
        return max_profit