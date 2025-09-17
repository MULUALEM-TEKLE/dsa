# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        res = []
        while q : 
            level_sum = 0
            for _ in range(len(q)) : 
                node = q.popleft()
                level_sum += node.val
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            res.append(level_sum)
        
        return 1+res.index(max(res))