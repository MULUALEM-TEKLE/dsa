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
        def dfs(root , tmp, cur_sum) : 
            if not root : return 
            
            cur_sum += root.val
            tmp.append(root.val)

            if not root.left and not root.right and cur_sum == targetSum : 
                res.append(tmp[:])
            
            dfs(root.left , tmp , cur_sum)
            dfs(root.right , tmp , cur_sum)
            tmp.pop()
        
        dfs(root , [] , 0)
        return res 