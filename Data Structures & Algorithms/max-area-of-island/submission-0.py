class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        maxx = 0

        def dfs(row, col):
            if row < 0 or col<0 or row>=rows or col>=cols:
                return 0
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            result = 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
            return result
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current = dfs(i, j)
                    maxx = max(maxx, current)
        return maxx
                

        