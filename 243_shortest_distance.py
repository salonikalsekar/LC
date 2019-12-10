class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:

        i1 = -1
        i2 = -1
        minDist = len(words)
        for i in range(len(words)):

            if words[i] == word1:
                i1 = i

            elif words[i] == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                minDist = min(minDist, abs(i2 - i1))

        return minDist