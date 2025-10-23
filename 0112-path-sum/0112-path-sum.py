# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def explore(node , cur) : 
            if not node : return False

            cur += node.val

            if not node.left and not node.right : 
                return cur == targetSum
            
            return explore(node.left , cur) or explore(node.right , cur)
        
        return explore(root , 0)