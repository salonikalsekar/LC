class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neigh = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        for i in range(len(board)):
            for j in range(len(board[0])):

                live_neigh = 0

                for n in neigh:
                    i1 = i + n[0]
                    j1 = j + n[1]

                    if (i1 >= 0 and i1 < len(board)) and (j1 >= 0 and j1 < len(board[0])):
                        if abs(board[i1][j1]) == 1:
                            live_neigh += 1

                if board[i][j] == 1 and (live_neigh < 2 or live_neigh > 3):
                    board[i][j] = -1

                if board[i][j] == 0 and live_neigh == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

