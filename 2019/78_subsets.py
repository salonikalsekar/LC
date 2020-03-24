class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.recur([[]], nums)

    def recur(self, res, nums):
        if not nums:
            return res

        temp = []

        for i in res:
            temp.append([nums[0]] + i)

        return self.recur(temp + res, nums[1:])