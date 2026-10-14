class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        result = 0
        for p in prices:
            if p<buy:
                buy = p
            result = max(result,p-buy)
        return result