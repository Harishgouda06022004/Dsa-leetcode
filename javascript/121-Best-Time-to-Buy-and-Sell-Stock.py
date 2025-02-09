class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n=len(prices)
        # # low=min(arr)
        # # high=max(arr)
        # max_profit=0
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         profit = prices[j] - prices[i]  # Calculate profit
        #         max_profit = max(max_profit, profit)
        # return max_profit
        min_price=float('inf')
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            else:
                max_profit=max(max_profit,price-min_price)
        return max_profit
                