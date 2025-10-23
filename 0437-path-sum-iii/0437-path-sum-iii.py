# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res  = 0

        freq = defaultdict(int)
        freq[0] = 1

        def dfs(root , freq , ps) : 
            if not root : return

            cs = ps + root.val
            x = cs - targetSum

            if x in freq : 
                self.res += freq[x]
            
            freq[cs] += 1 

            dfs(root.right , freq , cs)
            dfs(root.left , freq , cs)

            freq[cs] -= 1 
            
        
        dfs(root , freq , 0)

        return self.res