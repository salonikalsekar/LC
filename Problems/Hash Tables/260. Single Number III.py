from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = Counter(nums)
        res = []
        for k, v in sorted(temp.items(), key=lambda x: x[1]):
            if v == 1:
                res.append(k)
            else:
                break

        return res