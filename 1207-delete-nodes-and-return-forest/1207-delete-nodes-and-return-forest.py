# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res_set = set([root])

        def dfs(root) : 
            if not root : 
                return None 
            
            res = root 
            if root.val in to_delete : 
                res = None
                res_set.discard(root)
                if root.left : res_set.add(root.left)
                if root.right : res_set.add(root.right)
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return res
            
        dfs(root)
            
        return list(res_set)