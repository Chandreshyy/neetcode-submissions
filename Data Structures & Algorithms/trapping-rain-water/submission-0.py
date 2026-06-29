class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        dp_left = [height[0]]
        dp_right = [height[n-1]]
        res = 0

        for i in range(1, n-1):
            dp_left.append(max(dp_left[i-1], height[i]))
            dp_right.append(max(dp_right[i-1], height[n-1-i]))
        print(dp_left, dp_right)
        for i in range(1, n-1):
            res = res + max(0, min(dp_left[i-1], dp_right[n-1-i]) - height[i])

        return res

        