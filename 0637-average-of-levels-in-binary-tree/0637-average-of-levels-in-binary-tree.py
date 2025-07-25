# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        def bfs(root) : 
            q = deque()
            q.append(root)
            while q : 
                tmp = []
                lenq = len(q)
                for _ in range(len(q)) : 
                    node = q.popleft()
                    tmp.append(node.val)
                    if node.left : q.append(node.left)
                    if node.right : q.append(node.right)
                res.append(sum(tmp)/lenq)
        bfs(root)
        return res 
