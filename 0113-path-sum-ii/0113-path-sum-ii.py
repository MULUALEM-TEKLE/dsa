# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        path = []

        def dfs(root , cur) : 
            #base cases
            if not root : 
                return 
            
            # if cur > targetSum : 
            #     return

            path.append(root.val)
            cur += root.val

            if not root.left and not root.right and cur == targetSum : 
                res.append(path[:])

            dfs(root.left , cur)
            dfs(root.right , cur)
            path.pop()

        dfs(root , 0)

        return res
