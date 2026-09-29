class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = ((1,0), (0,1), (-1,0), (0,-1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
        count = 0
        queue_2 = deque()
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nrow, ncol = row+dr, col+dc
                if 0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    queue_2.append((nrow, ncol))
            if len(queue) == 0 and len(queue_2) != 0:
                temp = queue
                queue = queue_2
                queue_2 = temp
                count+=1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return count



        