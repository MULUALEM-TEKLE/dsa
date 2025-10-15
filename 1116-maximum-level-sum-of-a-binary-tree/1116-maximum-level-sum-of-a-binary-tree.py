# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        level = 1 
        data = {}

        while q : 
            level_sum = 0
            for _ in range(len(q)) : 
                node = q.popleft()
                level_sum += node.val

                if node.left : q.append(node.left)
                if node.right : q.append(node.right)

            data[level] = level_sum
            level += 1 

        max_level_sum = max(data.values())

        for level in data : 
            if data[level] == max_level_sum : 
                return level