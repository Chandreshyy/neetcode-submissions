class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        result = []

        def is_palindrome(s):
            res = True
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    res = False
                i+=1
                j-=1
            return res
                
        def backtrack(start, path):
            if start == n:
                result.append(path.copy())
                # print(f"base case path = {path.copy()}")
                return

            for i in range(start+1, n+1):
                first_part = s[start:i]
                sec_part = s[i:]
                is_pal = is_palindrome(first_part)
                # print(f"i={i}, start={start}, f_part={first_part}, s_part={sec_part}, path{path}, is_p={is_pal}")
                if is_pal:
                    path.append(first_part)
                    backtrack(i, path)
                    path.pop()
                
        backtrack(0, [])
        return result
                

