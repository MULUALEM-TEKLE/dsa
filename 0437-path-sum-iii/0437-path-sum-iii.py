# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root , ps , count) : 
            if not root : 
                return 
            cs = root.val + ps
            print(f"currnet sum is now {cs}") 
            x = cs - targetSum
            if x in freq.keys() : 
                print(f"adding to count is now {count}")
                count[0] += freq[x]
            
            if cs in freq.keys() : 
                freq[cs] += 1 
            else : 
                freq[cs] = 1

            dfs(root.left , cs , count)
            dfs(root.right , cs , count )
            freq[cs] -= 1
        
        count = [0]
        freq = {0 : 1}
        dfs(root, 0 , count)

        return count[0] 