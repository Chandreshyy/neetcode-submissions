# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_sum = float('-inf')

        def maxsum(node):
            if not node:
                return 0
            val = node.val
            left_sum = max(maxsum(node.left), 0)
            print(left_sum)
            right_sum = max(maxsum(node.right), 0)
            print(right_sum)
            self.max_sum = max(self.max_sum, left_sum + right_sum + val)
            print(self.max_sum)
            return val + max(left_sum, right_sum)

        maxsum(root)
        return self.max_sum

        