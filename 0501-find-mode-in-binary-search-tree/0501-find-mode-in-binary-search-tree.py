# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashmap = defaultdict(int)
        def dfs(root) : 
            if not root : 
                return 
            hashmap[root.val] += 1 
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(hashmap)
        res = []
        mode = max(hashmap.values())
        for key,val in hashmap.items() : 
            if val == mode : 
                res.append(key)
        return res 