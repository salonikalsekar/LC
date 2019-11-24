from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        h = {}
        for i in range(rowIndex + 1):
            h[i] = []

            for d in range(i + 1):
                h[i].append(factorial(i) // factorial(d) // factorial(i - d))

        return h[rowIndex]

