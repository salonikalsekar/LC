class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        WORDKEY = '$'
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})

            node[WORDKEY] = word
        matchedWords = []

        def backtracking(i, j, parent):
            letter = board[i][j]
            newCurr = parent[letter]

            ismatched = newCurr.pop(WORDKEY, False)
            if ismatched:
                matchedWords.append(ismatched)

            board[i][j] = '$'

            for newVal in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newRow = i + newVal[0]
                newCol = j + newVal[1]
                if newRow < 0 or newCol < 0 or newRow >= len(board) or newCol >= len(board[0]):
                    continue
                if not board[newRow][newCol] in newCurr:
                    continue
                backtracking(newRow, newCol, newCurr)

            board[i][j] = letter

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] in trie:
                    backtracking(i, j, trie)

        return matchedWords

