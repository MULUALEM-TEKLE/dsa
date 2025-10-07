# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        letters = list(string.ascii_lowercase)
        
        self.res = 'z' * 8501

        def dfs(root , cur) : 
            # base case 
            if not root : 
                return None

            # recursive part
            cur += letters[root.val]

            # leaf node 
            if not root.right and not root.left : 
                cur = cur[::-1]
                if cur < self.res :
                    self.res = cur  
                

            dfs(root.left , cur)
            dfs(root.right , cur)

        dfs(root , "")

        return self.res