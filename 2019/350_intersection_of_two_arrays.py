from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        l1 = len(nums1)
        l2 = len(nums2)

        if l2 < l1:
            l1, l2, nums1, nums2 = l2, l1, nums2, nums1

        d = Counter(nums1)

        for i in nums2:
            if i in d and d[i] > 0:
                res.append(i)
                d[i] -= 1

        return res

