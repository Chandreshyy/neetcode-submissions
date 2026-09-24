class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def backtrack(index, pos_count, neg_count, current):
            # print(f"current- {current}, index= {index}, pos_count= {pos_count},neg_count= {neg_count}")
            if index >= n*2:
                if pos_count==n and neg_count==n:
                    result.append(current)
                return
            if pos_count < n:
                backtrack(index+1, pos_count+1, neg_count, current+'(')
            if pos_count > neg_count:
                backtrack(index+1, pos_count, neg_count + 1, current+')')
            
        
        backtrack(0, 0, 0, "")
        return result

        