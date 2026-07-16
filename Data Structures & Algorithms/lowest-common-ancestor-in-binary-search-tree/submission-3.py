# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def is_ancestor(node, p, q):

            if node.val > p.val and node.val > q.val:
                 return is_ancestor(node.left, p, q)
            elif node.val < p.val and node.val < q.val:
                return is_ancestor(node.right, p, q)
            else:
                return node
        
        return is_ancestor(root, p, q)
        