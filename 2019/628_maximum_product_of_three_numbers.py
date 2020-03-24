import heapq


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # O(nlogn)
        #         nums = sorted(nums)
        #         return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

        # O(n)
        small = heapq.nsmallest(2, nums)
        large = heapq.nlargest(3, nums)
        return max(large[0] * large[1] * large[2], small[0] * small[1] * large[0])
