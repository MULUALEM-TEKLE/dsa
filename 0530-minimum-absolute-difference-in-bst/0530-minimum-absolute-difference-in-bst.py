# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float("inf")
        self.prev = None
        def dfs(root ) : 
            if not root : 
                return None
        
            dfs(root.left )
            if self.prev is not None : 
                self.min = min(self.min , root.val-self.prev)
            self.prev = root.val
            dfs(root.right )
        
        dfs(root )
        return self.min