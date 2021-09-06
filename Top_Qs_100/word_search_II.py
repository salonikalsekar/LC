class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node['$'] = w

        def traverse(i, j, board, parent):
            letter = board[i][j]
            newCurr = parent[letter]
            ismatched = newCurr.pop('$', False)
            if ismatched:
                output.append(ismatched)

            board[i][j] = '#'

            for newRC in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newR = newRC[0] + i
                newC = newRC[1] + j

                if newR < 0 or newR >= len(board) or newC < 0 or newC >= len(board[0]):
                    continue

                if board[newR][newC] not in newCurr:
                    continue

                traverse(newR, newC, board, newCurr)

            board[i][j] = letter

        output = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    traverse(i, j, board, trie)

        return output