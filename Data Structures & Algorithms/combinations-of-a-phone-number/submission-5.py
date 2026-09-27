class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        phone = {'2': "abc", '3': "def", '4': "ghi", '5': 
                   "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9':"wxyz"
        }

        result = []
        n = len(digits)
        if n == 0:
            return result

        def backtrack(index, current):

            if index == n:
                result.append(current)
                return
            
            cur_str = phone[digits[index]]

            for i in range(len(cur_str)):
                backtrack(index+1, current+cur_str[i])
            
        backtrack(0, '')
        return result

