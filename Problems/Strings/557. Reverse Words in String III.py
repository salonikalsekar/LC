class Solution:
    def reverseWords(self, s: str) -> str:
        result = list()
        res = s.split(" ")
        for i in res:
            result.append(i[::-1])

        return " ".join(result)