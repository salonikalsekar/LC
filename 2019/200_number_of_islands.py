class Solution:
    def __init__(self):
        self.seen = None

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if grid:
            row = len(grid)
            column = len(grid[0])
            visited = [[0] * column for i in range(row)]
            for i in range(row):
                for j in range(column):

                    if grid[i][j] == "1":
                        if not visited[i][j]:
                            count += 1
                            self.dfs(grid, visited, i, j)

            return count
        else:
            return 0

    def dfs(self, grid, visited, i, j):
        if i < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or j < 0 or grid[i][j] == "0" or visited[i][j] == 1:
            return

        visited[i][j] = 1

        self.dfs(grid, visited, i, j + 1)
        self.dfs(grid, visited, i, j - 1)
        self.dfs(grid, visited, i + 1, j)
        self.dfs(grid, visited, i - 1, j)







