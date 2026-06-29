class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        i, j = 0, n-1
        maxx = -1
        while i < j:
            cur = min(heights[i], heights[j]) * abs(j-i)
            print(cur)
            maxx = max(cur, maxx)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        
        return maxx
