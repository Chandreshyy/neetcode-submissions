class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        if n == 1:
            return 1
        
        i = 0
        mapp = {s[0]:0}
        maxx = 1
        j = 1
        while j < n:
            print(s[j])
            if s[j] not in mapp:
                mapp[s[j]] = j
                j += 1
                print(mapp, i, j, maxx)
            else:
                i = max(i, mapp[s[j]] + 1)
                mapp[s[j]] = j
                j += 1
            maxx = max(maxx, j - i)

        return maxx

