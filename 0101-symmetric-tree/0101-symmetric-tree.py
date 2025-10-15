# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def reverse(root) : 
    if not root : 
        return 
    root.left , root.right = root.right , root.left
    reverse(root.left)
    reverse(root.right)


def same(p , q) : 
    if not q and not p : 
        return True
    if not q or not p or q.val != p.val : 
        return False 
    # if p.val == q.val : 
    #     return True 
    
    return same(p.left , q.left) and same(p.right , q.right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        reverse(root.right)
        print(root.right)
        return same(root.left , root.right)