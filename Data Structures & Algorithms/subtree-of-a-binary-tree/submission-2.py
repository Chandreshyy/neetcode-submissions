# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return is_same(p.left, q.left) and is_same(p.right, q.right)
            else:
                return False
            
        def subtree(p, q):
            if not p:
                return False
            if is_same(p, q):
                return True
            return subtree(p.left, q) or subtree(p.right, q)
        
        return subtree(root, subRoot)
        