# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(root , cur) : 
            if not root : 
                return 
            
            cur += f'{root.val}->'
            
            if not root.left and not root.right : 
                res.append(cur[:-2])
            

            dfs(root.left , cur)
            dfs(root.right , cur)
        
        dfs(root , "")

        return res 