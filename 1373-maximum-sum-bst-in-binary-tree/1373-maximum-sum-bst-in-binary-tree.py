# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0 

        def solve(node) : 
            if not node : 
                return [True , inf , -inf , 0]
            
            left_bst , left_min , left_max , left_sum = solve(node.left)
            right_bst , right_min , right_max , right_sum = solve(node.right)

            if left_bst and right_bst and left_max < node.val < right_min : 
                cur_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum ,  cur_sum)

                return [True , min(left_min , node.val) , max(right_max , node.val) , cur_sum]
            
            else : 
                return [False , 0 , 0 , 0]
            
        
        solve(root)
        return self.max_sum