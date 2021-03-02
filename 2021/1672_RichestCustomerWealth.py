class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxVal = 0
        for i in range(0, len(accounts)):
            maxVal = max(maxVal, sum(accounts[i]))

        return maxVal