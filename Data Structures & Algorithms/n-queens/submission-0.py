class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def fill_board(row, col, new_board):
            for i in range(n):
                if i == col:
                    continue
                new_board[row][i] = '.'
            for j in range(n):
                if j == row:
                    continue
                new_board[j][col] = '.'
            i, j = row+1, col+1
            while i < n and j < n:
                new_board[i][j] = '.'
                i+=1
                j+=1
            i, j = row-1, col-1
            while i >= 0  and j >= 0:
                new_board[i][j] = '.'
                i-=1
                j-=1
            i, j = row+1, col-1
            while i < n  and j >= 0:
                new_board[i][j] = '.'
                i+=1
                j-=1
            i, j = row-1, col+1
            while i >= 0  and j < n:
                new_board[i][j] = '.'
                i-=1
                j+=1
        
        def backtrack(row, board):
            # print(f"row={row}, board={board}")
            if row == n:
                res = []
                for i in range(n):
                    res.append(''.join(board[i]))
                result.append(res)
                return

            for col in range(n):
                if board[row][col] == '.':
                    continue
                new_board = [row[:] for row in board]
                fill_board(row, col, new_board)
                new_board[row][col] = 'Q'
                backtrack(row+1, new_board)

        board = [['' for i in range(n)] for j in range(n)]
        result = []
        for i in range(n):
            new_board = [row[:] for row in board]
            fill_board(0, i, new_board)
            new_board[0][i] = 'Q'
            backtrack(1, new_board)
        return result
        

        