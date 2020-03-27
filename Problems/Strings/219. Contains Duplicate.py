from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictTemp = defaultdict(int)
        for idx, i in enumerate(nums):
            if i in dictTemp:
                if idx - dictTemp[i] <= k:
                    return True
            dictTemp[i] = idx
        return False