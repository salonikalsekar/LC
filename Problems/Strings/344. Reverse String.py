class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[::-1] does not reverse inplace, it creates a reverse copy
        # return s.reverse()

        # two pointers approach

        first = 0
        second = len(s) - 1

        while first < second:
            s[first], s[second] = s[second], s[first]
            first, second = first + 1, second - 1

