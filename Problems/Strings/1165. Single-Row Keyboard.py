class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        i = 0
        idx = 0
        idxSum = 0
        idx_prev = 0
        while i < len(word):
            idx = keyboard.index(word[i])
            idxSum += abs((idx_prev - idx))
            idx_prev = idx
            i += 1

        return idxSum