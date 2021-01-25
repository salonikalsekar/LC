from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)

        for string in strs:
            k = sorted(tuple(string))
            temp[str(sorted(tuple(string)))].append(string)

        return temp.values()