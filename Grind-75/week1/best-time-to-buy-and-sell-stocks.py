class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        min_price = 10001
        max_profit = 0 # the return value if nothing found
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(profit, max_profit)
        # it does not require the sliding window (double for loop) solution
        # because the maximum profit at any given point only depends on the lowest price seen so far and the current price
        
        return max_profit
