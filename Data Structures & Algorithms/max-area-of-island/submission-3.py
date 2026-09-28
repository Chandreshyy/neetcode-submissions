from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxx = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = 0
            area = 1

            while queue:
                r, c = queue.popleft()
                if r+1 < rows and grid[r+1][c] == 1:
                    area+=1
                    queue.append((r+1, c))
                    grid[r+1][c] = 0
                if c+1 < cols and grid[r][c+1] == 1:
                    area+=1
                    queue.append((r, c+1))
                    grid[r][c+1] = 0
                if r-1 >= 0 and grid[r-1][c] == 1:
                    area+=1
                    queue.append((r-1, c))
                    grid[r-1][c] = 0
                if c-1 >= 0 and grid[r][c-1] == 1:
                    area+=1
                    queue.append((r, c-1))
                    grid[r][c-1] = 0
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxx = max(maxx, bfs(i, j))
        
        return maxx


