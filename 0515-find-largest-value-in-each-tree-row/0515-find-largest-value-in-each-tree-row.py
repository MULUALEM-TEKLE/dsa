# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root : 
            return []

        q = deque([root])

        while q : 
            rowmax = float('-inf')
            for _ in range(len(q)) : 
                node = q.popleft()
                rowmax = max(rowmax , node.val)

                if node.left : q.append(node.left)
                if node.right : q.append(node.right)

            res.append(rowmax)
        

        return res
