class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        # print(queue)
        
        while queue:
            row, col = queue.popleft()
            cur_value = grid[row][col]
            if row+1 < rows and grid[row+1][col] == INF:
                grid[row+1][col] = cur_value + 1
                queue.append((row+1, col))
            if col+1 < cols and grid[row][col+1] == INF:
                grid[row][col+1] = cur_value + 1
                queue.append((row, col+1))
            if row-1 >= 0 and grid[row-1][col] == INF:
                grid[row-1][col] = cur_value + 1
                queue.append((row-1, col))
            if col-1 >= 0 and grid[row][col-1] == INF:
                grid[row][col-1] = cur_value + 1
                queue.append((row, col-1))
        


