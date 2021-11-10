class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, x) for x in (y - x for x, y in zip(prices, prices[1:])))