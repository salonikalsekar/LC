from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        dict_t = Counter(t)
        required = len(dict_t)

        formed = 0
        ans = float('inf'), None, None
        window_dict = {}

        while r < len(s):

            ch = s[r]

            window_dict[ch] = window_dict.get(ch, 0) + 1

            if ch in dict_t and dict_t[ch] == window_dict[ch]:
                formed += 1

            while l <= r and formed == required:
                ch = s[l]

                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r

                window_dict[ch] -= 1

                if ch in dict_t and dict_t[ch] > window_dict[ch]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]