# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = defaultdict(int)
        output = []
        def dfs(root) : 
            if not root : 
                return 
            res[root.val] += 1 
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        mode = max(res.values())
        for key,val in res.items() : 
            if val == mode : 
                output.append(key)
        
        return output


