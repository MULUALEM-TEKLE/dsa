# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root , targetSum) : 
            if not root : 
                return False
            
            targetSum -= root.val

            if not root.left and not root.right : 
                return targetSum == 0
            
            return dfs(root.left , targetSum) or dfs(root.right , targetSum)

        return dfs(root, targetSum)