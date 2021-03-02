class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        temp = {}
        for i in nums:
            temp[i] = 1

        for i in range(1, len(nums) + 1):
            if i not in temp:
                res.append(i)

        return res