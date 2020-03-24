from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in seen:
                for data in seen[nums[i]]:
                    val = i - data
                    if val <= k:
                        return True

                seen[nums[i]].append(i)

            else:
                seen[nums[i]].append(i)

        return False