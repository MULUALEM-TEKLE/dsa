# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # lets do preorder traversal
        # check if node is null
        if not root : 
            return False
        targetSum -= root.val
        # check if we're at a leaf node and if target sum is reached return true
        if not root.right and not root.left and targetSum == 0:
            return True
        return self.hasPathSum(root.left , targetSum) or self.hasPathSum(root.right , targetSum)
        # check left
        # check right
        # if nothing found return false