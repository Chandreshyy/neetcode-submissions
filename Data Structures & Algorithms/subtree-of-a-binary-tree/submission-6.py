# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def issame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return issame(p.left, q.left) and issame(p.right, q.right)
            return False
        
        def issubtree(root, subroot):
            if not root:
                return subroot == None
            
            if issame(root, subroot):
                return True
            return issubtree(root.left, subroot) or issubtree(root.right, subroot)

        return issubtree(root, subRoot)
        