class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) != 0:
            res = []
            s = set(nums)

            for i in range(1, len(nums) + 1):
                if i not in s:
                    res.append(i)

            return res
