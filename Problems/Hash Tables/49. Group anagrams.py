from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for word in strs:
            temp[tuple(sorted(word))].append(word)

        return temp.values()
