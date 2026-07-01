class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stackk = []
        mapping = {')':'(', '}': '{', ']': '['}

        for i in s:
            if i in mapping:
                if not stackk or mapping[i] != stackk[-1]:
                    return False
                stackk.pop()
            else:
                stackk.append(i)        
        if stackk:
            return False
        return True
