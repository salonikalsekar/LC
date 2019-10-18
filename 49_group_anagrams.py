class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        final = []
        for i in range(len(strs)):
            tempList = list(strs[i])

            tup = tuple(sorted(tempList))

            k = d.keys()
            if tup not in k:
                d[tup] = [strs[i]]
            else:
                d[tup].append(strs[i])

        for i in d.values():
            final.append(i)

        return final


