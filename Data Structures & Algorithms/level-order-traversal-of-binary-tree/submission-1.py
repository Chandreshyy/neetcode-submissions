# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        res = []
        queue = deque([root])
        # res.append([root.val])

        while queue:
            cur = []
            i, n = 0, len(queue)
            while i < n:
                temp_node = queue.popleft()
                cur.append(temp_node.val)
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
                i += 1
            res.append(cur)
        
        return res
            
            
        

        # while 
        