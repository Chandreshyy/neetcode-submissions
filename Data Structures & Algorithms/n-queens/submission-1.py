class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        rows = set()
        diag = set()
        anti_diag = set()

        board = [['.']*n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(i) for i in board])
                return
            
            for col in range(n):
                if row in rows or col in cols or row-col in diag or row+col in anti_diag:
                    continue

                rows.add(row)
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)
                board[row][col] = 'Q'

                backtrack(row+1)

                board[row][col] = '.'
                rows.remove(row)
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)
        
        backtrack(0)
        return result


