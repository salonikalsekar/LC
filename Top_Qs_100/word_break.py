class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        visited = []
        q = deque()
        q.append(0)

        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):

                if s[start:end] in wordDict:
                    q.append(end)

                    if end == len(s):
                        return True
                    visited.append(start)

        return False