# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def reverse_tree(root) : 
            if not root : 
                return 

            root.left , root.right = root.right , root.left
            reverse_tree(root.left)
            reverse_tree(root.right)

            return root
        
        def same_tree(a , b) : 
            if not a and not b : 
                return True 
            if not a or not b or a.val != b.val  : 
                return False 
            return same_tree(a.left , b.left) and same_tree(a.right , b.right)
        
        if not root.left and not root.right : 
            return True 
        
        a = root.left 
        b = reverse_tree(root.right)

        return same_tree(a , b)