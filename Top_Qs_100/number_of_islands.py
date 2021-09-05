class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(i, j, visited, grid):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] == 1 or grid[i][j] == "0":
                return

            visited[i][j] = 1

            traverse(i, j + 1, visited, grid)
            traverse(i, j - 1, visited, grid)
            traverse(i + 1, j, visited, grid)
            traverse(i - 1, j, visited, grid)

        count = 0

        visited = [[0] * len(grid[0]) for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    traverse(i, j, visited, grid)

        return count




