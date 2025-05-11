# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted = []
        self.helper(root, sorted)
        return sorted[k-1]

    def helper(self, root, sorted):
        if not root : 
            return
        
        self.helper(root.left, sorted)
        sorted.append(root.val)
        self.helper(root.right, sorted)

    