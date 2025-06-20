# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque()

        if root : 
            q.append(root)

        while q : 
            avg = 0
            len_q = len(q)
            for _ in range(len_q) : 
                node = q.popleft()
                avg += node.val
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            res.append(avg/len_q)
        return res 
            