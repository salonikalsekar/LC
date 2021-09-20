class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        c = {}
        currSum = 0
        for i in nums:
            currSum += i

            if currSum == k:
                res += 1

            if currSum - k in c:
                res += c[currSum - k]

            if currSum in c:
                c[currSum] += 1
            else:
                c[currSum] = 1

        return res