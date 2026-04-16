# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0 

        def walk(node , go_left , cur_len) : 
            if not node : return 
            self.max_len = max(self.max_len , cur_len)

            if go_left : 
                walk(node.left , False , cur_len + 1)
                walk(node.right , True , 1)
            else : 
                walk(node.right , True , cur_len+1)
                walk(node.left , False , 1)
        walk(root.left , False , 1)
        walk(root.right , True , 1)

        return self.max_len