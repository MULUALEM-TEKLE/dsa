# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root : return []

        res = []
        q = deque([root])

        while q : 
            tmp = []
            q_len = len(q)
            for _ in range(q_len) : 
                node = q.popleft()
                tmp.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            res.append(round(sum(tmp)/q_len , 5))
        
        print(res)
        return res