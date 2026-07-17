# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []
        s = []
        s.append(root)

        while s:
            temp = s.pop()
            temp_left = temp.left
            temp_right = temp.right
            # print(temp.val)
            if temp_left:
                temp.left = None
                s.append(temp)
                s.append(temp_left)
            else:
                res.append(temp.val)
                if temp_right:
                    s.append(temp_right)

        print(res)
        return res[k-1]

