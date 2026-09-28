class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = '0'

            while queue:
                r, c = queue.popleft()
                if r+1 < rows and grid[r+1][c] == '1':
                    grid[r+1][c] = '0'
                    queue.append((r+1, c))
                if r-1 >= 0 and grid[r-1][c] == '1':
                    grid[r-1][c] = '0'
                    queue.append((r-1, c))
                if c+1 < cols and grid[r][c+1] == '1':
                    grid[r][c+1] = '0'
                    queue.append((r, c+1))
                if c-1 >= 0 and grid[r][c-1] == '1':
                    grid[r][c-1] = '0'
                    queue.append((r, c-1))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        
        return count

                

