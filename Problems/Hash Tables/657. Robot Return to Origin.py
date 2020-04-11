class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movesDict = {'U': 2, 'D': -2, 'L': -1, 'R': 1}
        origin = 0
        for ch in moves:
            origin += movesDict[ch]

        if origin:
            return False
        else:
            return True