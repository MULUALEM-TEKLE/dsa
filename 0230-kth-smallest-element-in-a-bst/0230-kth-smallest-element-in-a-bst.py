# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [None]
        def dfs(root , k) : 
            if not root or res[0] : 
                return None 
            
            dfs(root.left , k)
            k[0] -= 1 
            if k[0] == 0 : 
                res[0] = root.val
                return
            dfs(root.right , k)

        dfs(root , [k])
        return res[0]