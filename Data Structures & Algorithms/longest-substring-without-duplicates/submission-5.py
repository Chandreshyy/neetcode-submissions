class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        i = 0
        maxx = 0
        mapp = {}

        for j in range(n):
            if s[j] in mapp:
                i = max(i, mapp[s[j]] + 1)
            maxx = max(maxx, j - i + 1)
            mapp[s[j]] = j

        return maxx

