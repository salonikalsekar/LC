class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        s_dict = dict(zip(range(0, 26), [0] * 26))
        p_dict = dict(zip(range(0, 26), [0] * 26))

        for i in p:
            p_dict[ord(i) - ord('a')] += 1

        step = len(p)
        res = []

        for i in range(len(s)):

            if i >= step:
                s_dict[ord(s[i - step]) - ord('a')] -= 1

            s_dict[ord(s[i]) - ord('a')] += 1

            if s_dict == p_dict:
                res.append(i - step + 1)

        return res


