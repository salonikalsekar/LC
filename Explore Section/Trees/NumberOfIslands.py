class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        rows = len(grid)
        columns = len(grid[0])
        visited = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    if not visited[i][j]:
                        count += 1
                        self.dfs(i, j, visited, rows, columns, grid)
        return count

    def dfs(self, i, j, visited, rows, columns, grid):
        if i < 0 or i > rows - 1 or j < 0 or j > columns - 1 or visited[i][j] == 1 or grid[i][j] == "0":
            return

        visited[i][j] = 1

        self.dfs(i + 1, j, visited, rows, columns, grid)
        self.dfs(i - 1, j, visited, rows, columns, grid)
        self.dfs(i, j + 1, visited, rows, columns, grid)
        self.dfs(i, j - 1, visited, rows, columns, grid)

