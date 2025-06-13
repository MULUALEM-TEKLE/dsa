# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root 
        stack = []
        k_ = [k]
       

        while stack or cur : 
            while cur  : 
                stack.append(cur)
                cur = cur.left 
            cur = stack.pop()
            k_[0] -= 1
            if k_[0] == 0 : 
                return cur.val
            print(cur.val)
            cur = cur.right

        