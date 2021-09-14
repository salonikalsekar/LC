class Solution:
    def reverseWords(self, s: List[str]) -> None:

        def reverseWord(s, start, end):

            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        left = 0

        for idx, ch in enumerate(s):
            if ch == ' ':
                reverseWord(s, left, idx - 1)
                left = idx + 1

        reverseWord(s, left, len(s) - 1)
        reverseWord(s, 0, len(s) - 1)
