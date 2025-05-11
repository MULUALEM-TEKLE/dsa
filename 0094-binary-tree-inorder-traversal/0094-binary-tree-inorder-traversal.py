# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._helper(root, result)
        return result
        
    def _helper(self, root: Optional[TreeNode], result: List[int] ): 
        if not root :
            return
        self._helper(root.left , result)
        result.append(root.val)
        self._helper(root.right, result)