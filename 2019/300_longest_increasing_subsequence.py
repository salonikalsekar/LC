class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for i in nums:
            pos = bisect.bisect_left(tail, i)
            tail[pos:pos + 1] = [i]

        return len(tail)