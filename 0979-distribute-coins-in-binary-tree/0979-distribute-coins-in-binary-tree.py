# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0 

        def balance(node) : 
            if not node : 
                return 0 

            
            left_balance = balance(node.left)
            right_balance = balance(node.right)

            self.moves += abs(left_balance) + abs(right_balance)

            return node.val + left_balance + right_balance - 1

        balance(root)
       
        return self.moves 