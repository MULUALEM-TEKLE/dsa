# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0 

        def dfs(root , maxval) : 
            if not root : return

            if root.val >= maxval : 
                self.res += 1 
            
            maxval = max(root.val , maxval)

            dfs(root.left , maxval)
            dfs(root.right , maxval)

        
        dfs(root , root.val)

        return self.res