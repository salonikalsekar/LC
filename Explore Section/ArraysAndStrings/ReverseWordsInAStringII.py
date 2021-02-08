class Solution:
    def reverseWords(self, s: List[str]) -> None:

        def reverseWord(start, end):

            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        left = 0
        reverseWord(left, len(s) - 1)

        for idx, ch in enumerate(s):
            if ch == ' ':
                reverseWord(left, idx - 1)
                left = idx + 1

        reverseWord(left, len(s) - 1)