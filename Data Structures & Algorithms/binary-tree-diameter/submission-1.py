# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def max_depth(node):
            if not node:
                return 0
            return 1 + max(max_depth(node.left), max_depth(node.right))

        def max_d(node, max_dia):
            if not node:
                return 0
            cur_dia = max_depth(node.left) + max_depth(node.right)
            max_dia = max(cur_dia, max_d(node.left, max_dia), max_d(node.right, max_dia), max_dia)
            return max_dia
        
        max_dia = max_d(root, 0)
        return max_dia



