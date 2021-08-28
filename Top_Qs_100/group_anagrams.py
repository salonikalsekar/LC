from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        result = defaultdict(list)

        for item in strs:
            k = tuple(sorted(item))
            result[k].append(item)

        return result.values()
