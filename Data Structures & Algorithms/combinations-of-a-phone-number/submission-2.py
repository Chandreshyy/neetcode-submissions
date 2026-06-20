class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {'2': "abc", '3': "def", '4': "ghi", '5': 
                   "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9':"wxyz"
        }

        res = []
        n = len(digits)
        if not digits:
            return []

        def solve(index, cur):
            if index == n:
                res.append("".join(cur))
                return

            digit = digits[index]
            chars = phone[digit]
            
            for ch in chars:
                cur.append(ch)
                solve(index + 1, cur)
                cur.pop()
        
        solve(0, [])
        return res

            

        
        
        
        
        