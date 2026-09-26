class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        n = len(word)

        def backtrack(i, j, index):
            if index == n:
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            
            cur_char = board[i][j]
            if cur_char != word[index]:
                return False
            board[i][j] = '#'
            result = (
                backtrack(i-1, j, index+1)
                or backtrack(i+1, j, index+1)
                or backtrack(i, j-1, index+1)
                or backtrack(i, j+1, index+1)
            )
            board[i][j] = cur_char
            return result
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False

        