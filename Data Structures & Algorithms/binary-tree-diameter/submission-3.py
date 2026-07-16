# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_dia = 0

        def max_depth(node):
            if not node:
                return 0
            left, right = max_depth(node.left), max_depth(node.right)
            self.max_dia = max(self.max_dia, left + right)
            return 1 + max(left, right)
        
        max_depth(root)
        return self.max_dia



