# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        node = root
        stack = []
        stack.append(node)
        i = 0
        while stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            node = node.right
        
        

            
                