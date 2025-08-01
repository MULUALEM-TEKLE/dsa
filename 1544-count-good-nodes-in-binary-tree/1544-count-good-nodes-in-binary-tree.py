# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root , max_val ) : 
            if not root : return 
            
            if root.val >= max_val : 
                self.res += 1 
            max_val = max(max_val , root.val)

            if not root.left and not root.right : 
                return 
            
            dfs(root.left , max_val)
            dfs(root.right , max_val)

        
        dfs(root , float('-inf'))
        
        return  self.res