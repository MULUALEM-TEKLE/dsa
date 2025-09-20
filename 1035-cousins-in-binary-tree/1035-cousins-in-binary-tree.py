# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        candidates = {}
        def dfs(node , parent , level) : 
            if not node : 
                return 
            
            if node.val == x or node.val == y : 
                candidates[node.val] = [parent.val if parent else None , level]
            level += 1 
            dfs(node.left , node , level)
            dfs(node.right , node , level)
        
        dfs(root , None , 0)
        print(candidates)
        if candidates[x][0] != candidates[y][0] and candidates[x][1] == candidates[y][1] : return True 
        return False 
