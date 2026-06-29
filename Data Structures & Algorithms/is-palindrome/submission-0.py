class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        n = len(new_s)
        for i in range((n+1)//2):
            # print(new_s[i], new_s[n-1-i])
            if new_s[i] == new_s[n-1-i]:
                continue
            else:
                return False
        
        return True
        
        