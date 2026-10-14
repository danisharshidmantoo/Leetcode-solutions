class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0
        buy = prices[0]
        for p in prices:
            if p>buy:
                result += (p-buy)
                buy = p
            elif p<buy:
                buy = p
        return result