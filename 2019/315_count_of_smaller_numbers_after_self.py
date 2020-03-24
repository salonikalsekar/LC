class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tmp = []
        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            index = bisect.bisect_left(tmp, nums[i])
            res[i] = index
            tmp.insert(index, nums[i])

        return res

