class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)

        res = []

        plen = len(p)
        i = 0
        j = i + plen
        slen = len(s)

        if slen < plen:
            return []

        while j <= slen:
            if sorted(s[i:j]) == p:
                res.append(i)

            i += 1
            j = i + plen

        return res
