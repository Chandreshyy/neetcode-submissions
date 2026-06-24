class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
    
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                row_key  = (num, 'row', i)
                col_key  = (num, 'col', j)
                box_key  = (num, 'box', i//3, j//3)
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        
        return True
        # def _box_no(i, j):
        #     return  int(18 + (i//3)*3 + j//3)

        # # sets = [set()]*27
        # sets = []
        # for i in range(27):
        #     sets.append(set())
        
        # for i in range(9):
        #     for j in range(9):
        #         num = board[i][j]
        #         if num == '.':
        #             continue
        #         box_no = _box_no(i,j)
        #         # print(i, j, num, box_no, sets)
        #         if num in sets[i] or num in sets[9+j] or num in sets[box_no]:
        #             return False
        #         sets[i].add(num)
        #         sets[9+j].add(num)
        #         sets[box_no].add(num)
        
        # return True
        
            
