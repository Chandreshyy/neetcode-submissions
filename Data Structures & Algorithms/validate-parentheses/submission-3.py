class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stackk = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stackk.append(i)
                print(stackk)
            elif i == ')':
                if not stackk or stackk[-1] != '(':
                    return False
                stackk.pop()
            elif i == '}':
                if not stackk or stackk[-1] != '{':
                    return False
                stackk.pop()
            else:
                print(i)
                print(stackk)
                if not stackk or stackk[-1] != '[':
                    return False
                stackk.pop()
        
        if stackk:
            return False
        return True
