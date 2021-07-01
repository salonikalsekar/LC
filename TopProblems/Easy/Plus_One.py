class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = map(str, digits)
        s = int(''.join(n))
        return str(s + 1)[::]