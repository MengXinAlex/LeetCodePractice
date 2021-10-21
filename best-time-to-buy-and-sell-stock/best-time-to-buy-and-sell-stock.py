class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minV = 0, 10**4+1
        for i in prices:
            if i < minV:
                minV = i
            elif i - minV > maxP:
                maxP = i - minV
        return maxP