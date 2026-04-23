# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #DFS: obvious because we want to go far down first and then come back up
        #tree is some type of recursion

        res = []
        stack = []

        cur = root

        #tree iterative approach = WHILE LOOP!!!!!

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left

            else:
                cur = stack.pop()

        return res

        #append cur
        #we set cur to left until there are no lefts but in the meantime 
        #we add the right to the stack and save it for later to do it in correct order



        #stack because there are no pointers pointching child back to parent 
        #so we do it ourselves with popping stack