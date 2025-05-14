# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def hasSum(root , sum_ , targetSum) : 
    if not root : 
        return False
    
    sum_ += root.val

    if not root.left and not root.right : 
            return sum_ == targetSum
    return  hasSum(root.left, sum_,  targetSum) or  hasSum(root.right, sum_,  targetSum)
  

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_ = 0
        return hasSum(root, sum_ , targetSum)


                