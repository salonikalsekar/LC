class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = map(str, digits)
        s = ''.join(s)
        res = str(int(s) + 1)
        ans = list(map(int, res))
        return(ans)