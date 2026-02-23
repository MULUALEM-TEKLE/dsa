# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max =  -inf
        def find_max(root) : 
            if not root : 
                return 0
            
            left = max(0 , find_max(root.left))
            right = max(0 , find_max(root.right))

            cur_sum = left + root.val + right

            self.global_max = max(self.global_max , cur_sum)

            return root.val + max(left , right)

        find_max(root)
        return self.global_max 