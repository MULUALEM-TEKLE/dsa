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
    print(f"current node {root.val} and sum {sum_}\n")

    if not root.left and not root.right : 
        print("got to a leaf node")
        if sum_ == targetSum  : 
            print("found my sum")
            return True
    if hasSum(root.left, sum_,  targetSum) : 
        return True
    if hasSum(root.right, sum_,  targetSum) : 
        return True

    sum_ -= root.val
    print(f"backtracking with sum {sum_}")
    return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_ = 0
        return hasSum(root, sum_ , targetSum)


                