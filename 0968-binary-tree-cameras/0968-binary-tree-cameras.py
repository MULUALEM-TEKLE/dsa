# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0

        def dfs(node) : 
            if not node : return 2

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0 : 
                self.cameras += 1 
                return 1 

            if left == 1 or right == 1 : 
                return 2 


            return 0 

        if dfs(root) == 0 : 
            self.cameras += 1 

        return self.cameras 
    

    # my name is wini kebede
    # my name is wini kbede 
    # today is staurday and I love my wife, she is a bit annoying but I can tolerate her some how , her annoying ass can be very annoying sometimes but its fine, I can live with her, living with her is like living with a bear 

    # today is staurday and i love my wife she is bit annoying but ican tolerate her some how her annoying ass can be very annoying sometimes but its fine i can live with her living with her is like living with a bear 
    