# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(s , t) : 
            if not s and not t : 
                return True  
            if not s or not t : 
                return False 
            if s.val != t.val : 
                return False
            
            return isEqual(s.left , t.left) and isEqual(s.right , t.right)
            
        def dfs(root) : 
            if not root : return False 

            if isEqual(root , subRoot) : return True

            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
