class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left = [0]*n
        right = [0]*n

        stack = []
        for i in range(n):
            cur = heights[i]
            while stack and heights[stack[-1]] >= cur:
                temp = stack.pop()
                right[temp] = i
            stack.append(i)
        # print(stack)
        while len(stack) > 0:
            right[stack[-1]] = n
            stack.pop()

        stack = []
        for i in range(n):
            cur = heights[i]
            while stack and heights[stack[-1]] >= cur:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        # print(right, left)
        maxa = 0
        for i in range(n):
            l = left[i]
            r = right[i]
            width = r - l - 1
            area = heights[i]*width
            maxa = max(area, maxa)
        return maxa