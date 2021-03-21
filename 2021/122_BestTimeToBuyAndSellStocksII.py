class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = 0

        for p in range(1, len(prices)):
            if prices[p] > prices[p - 1]:
                max_price += prices[p] - prices[p - 1]

        return max_price