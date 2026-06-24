class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def _box_no(i, j):
            return  int(18 + (i//3)*3 + j//3)

        sets = []
        for i in range(27):
            sets.append(set())
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                box_no = _box_no(i,j)
                # print(i, j, num, box_no, sets)
                if num in sets[i] or num in sets[9+j] or num in sets[box_no]:
                    return False
                sets[i].add(num)
                sets[9+j].add(num)
                sets[box_no].add(num)
        
        return True
        
            
