# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root : 
            return []

        res = []

        def dfs(root , targetSum , tmp) : 
            if not root : 
                return 
            
            tmp.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0 : 
                res.append(tmp[:])
               
  
            
            dfs(root.left , targetSum , tmp )
            dfs(root.right , targetSum , tmp )
            tmp.pop()
        
        dfs(root , targetSum , [] )

        return res


