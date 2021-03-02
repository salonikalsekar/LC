from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp = Counter(nums)
        s = sorted(temp)
        res = []
        for k, v in temp.items():
            if v != 1:
                res.append(k)

        return res

