from collections import Counter
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = Counter(nums)
        if count[max(count.keys(), key = count.get)] > len(nums)//2:
            return max(count.keys(), key = count.get) == target