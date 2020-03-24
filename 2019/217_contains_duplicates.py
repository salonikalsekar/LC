from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        ans = False

        for i in nums_count.values():
            if i > 1:
                return True

        return ans



