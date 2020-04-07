class Solution:
    def isValid(self, s: str) -> bool:
        setCheck = {')':'(', '}':'{', ']': '[' }
        res = []
        for i in s:
            if res and i in setCheck:
                if setCheck[i] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)
        return not res