class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        while n not in set1:
            set1.add(n)
            if n == 1:
                return True
            sumVal = 0
            st = str(n)
            for i in st:
                sumVal += int(i) ** 2
                n = sumVal
        return False