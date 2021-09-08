class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        ssum = 0

        while n != 1:
            ssum = 0
            for i in str(n):
                ssum += int(i) ** 2

            if ssum in s:
                return False

            s.add(ssum)
            n = ssum

        return True