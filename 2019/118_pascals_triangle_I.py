from math import factorial


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        h = {}

        for i in range(numRows):
            h[i] = []

            for d in range(i + 1):
                h[i].append(factorial(i) // factorial(d) // factorial(i - d))

        return h.values()