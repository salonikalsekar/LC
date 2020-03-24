from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        i = 0
        j = 0

        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                box = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    rows[i][board[i][j]] = rows[i].get(board[i][j], 0) + 1
                    columns[j][board[i][j]] = columns[j].get(board[i][j], 0) + 1
                    boxes[box][board[i][j]] = boxes[box].get(board[i][j], 0) + 1

                    if rows[i][board[i][j]] > 1 or columns[j][board[i][j]] > 1 or boxes[box][board[i][j]] > 1:
                        return False

        return True






