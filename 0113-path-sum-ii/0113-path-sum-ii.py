# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(root , target) : 
            if not root : 
                return 

            subset.append(root.val)
            target -= root.val

            
            if not root.left and not root.right and target == 0 : 
                res.append(subset[:])
            
            dfs(root.left , target)
            dfs(root.right , target)
            subset.pop()
        
        dfs(root , targetSum)
        return res