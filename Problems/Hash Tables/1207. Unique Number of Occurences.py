from collections import defaultdict, Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tempDict = Counter(arr)
        return len(tempDict.values()) == len(set(tempDict.values()))