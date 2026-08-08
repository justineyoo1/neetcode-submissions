# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def height(curr):
            nonlocal res

            if curr is None:
                return 0
        
            left = height(curr.left)
            right = height(curr.right)

            diff = abs(left - right)

            if diff > 1:
                res = False
            
            return 1 + max(left, right)

        height(root)
        return res
            
        