# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def solve(curr, p, q):
            if curr.val >= p.val and curr.val <= q.val:
                return curr
            if curr.val > q.val:
                return solve(curr.left, p, q)
            else:
                return solve(curr.right, p, q)
        if p.val > q.val:
            return solve(root, q, p)
        return solve(root, p, q)

        