class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        if n != len(t):
            return False
        
        count = {}

        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for j in t:
            if j not in count or count[j] == 0:
                return False
            else:
                count[j] -= 1
        
        for k in count:
            if count[k] != 0:
                return False

        return True
        