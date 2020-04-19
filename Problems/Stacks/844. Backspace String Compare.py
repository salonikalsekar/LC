class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        stackS = []
        stackT = []

        for s in S:
            if stackS and s == '#':
                stackS.pop()
            else:
                if s != '#':
                    stackS.append(s)

        for t in T:
            if stackT and t == '#':
                stackT.pop()
            else:
                if t != '#':
                    stackT.append(t)
        return ''.join(stackS) == ''.join(stackT)