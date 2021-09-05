class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i, j, board, word):

            if not word:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if word[0] == board[i][j]:
                board[i][j] = '#'

                if traverse(i, j + 1, board, word[1:]) or traverse(i, j - 1, board, word[1:]) or traverse(i + 1, j,
                                                                                                          board, word[
                                                                                                                 1:]) or traverse(
                        i - 1, j, board, word[1:]):
                    return True
                board[i][j] = word[0]

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if traverse(i, j, board, word):
                    return True

        return False


