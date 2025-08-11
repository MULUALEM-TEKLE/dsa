# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)

        def dfs(root) : 
            if not root : return 0 

            rv = root.val + dfs(root.left) + dfs(root.right)
            d[rv] += 1 

            return rv
        
        dfs(root)
        mx = max(d.values())

        return [k for k,v in d.items() if v == mx]