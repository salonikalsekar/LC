class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return

        tot = 0
        i = 0
        d = {0: 1}
        x = 0

        while x < len(nums):
            i += nums[x]
            if i - k in d:
                tot += d[i - k]
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            x += 1

        return tot