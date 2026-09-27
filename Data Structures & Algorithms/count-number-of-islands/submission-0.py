class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if grid[row][col] == '0':
                return
            
            grid[row][col] = '0'

            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row, col-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i, j)
        
        return count