class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        minVal = prices[0]
        for i in prices:
            if i < minVal:
                minVal = i
            if maxDiff < abs(i - minVal):
                maxDiff = max(maxDiff, abs(i - minVal))

        return maxDiff


