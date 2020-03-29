from collections import Counter
import sys


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        tempDict = Counter(A)
        maxNum = -1
        for k, v in sorted(tempDict.items()):
            if v == 1 and k > maxNum:
                maxNum = k

        return maxNum