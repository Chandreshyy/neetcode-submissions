# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        self.res = 0

        def countgoodnodes(node, maxx):
            if not node:
                return 
            if node.val < maxx:
                countgoodnodes(node.left, maxx)
                countgoodnodes(node.right, maxx)
            else:
                self.res += 1
                maxx = node.val
                countgoodnodes(node.left, maxx)
                countgoodnodes(node.right, maxx)
        
        countgoodnodes(root, root.val)
        return self.res


        