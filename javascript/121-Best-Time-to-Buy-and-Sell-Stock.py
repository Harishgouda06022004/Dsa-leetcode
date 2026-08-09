class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=float('inf')
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            profit=prices[i]-min_price
            if profit>0:
                max_profit=max(max_profit,profit)
        return max_profit
