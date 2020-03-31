class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        return nums1Set & nums2Set

# Facebook interview question
# O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
# You are told the lists are sorted.
# Cases to take into consideration include:
# duplicates, negative values, single value lists, 0's, and empty list arguments.
# Other considerations might include
# sparse arrays.

# ..to be continued