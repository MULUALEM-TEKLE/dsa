# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a , b) : 
            if not a and not b : 
                return True 
            if (not a or not b) or (a.val != b.val) : 
                return False
            
            return same(a.left , b.left) and same(a.right , b.right)
        
        def dfs(root) : 
            if not root : 
                return False
            
            if root.val == subRoot.val : 
                if same(root , subRoot) : return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)