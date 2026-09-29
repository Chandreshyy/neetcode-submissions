class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            row, col = queue.popleft()
            cur_value = grid[row][col]
            for dr, dc in directions:
                nrow, ncol = row + dr, col + dc
                if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] == INF:
                    grid[nrow][ncol] = cur_value + 1
                    queue.append((nrow, ncol))
        


