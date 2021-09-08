class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strings:
            temp = []
            for i in range(1,len(s)):
                temp.append((ord(s[i])-ord(s[i-1]))%26) # relative position of i wrt to (i-1)
            ans[tuple(temp)].append(s)
        return ans.values()