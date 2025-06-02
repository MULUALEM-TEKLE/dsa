# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []

        res = []
        q = deque([root])
        level = 0

        while len(q) : 
            tmp = []
            for _ in range(len(q)) : 
                node = q.popleft()
                tmp.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            level += 1 
            if level % 2 == 0 : 
                tmp.reverse()
                res.append(tmp)
            else : 
                res.append(tmp)

        return res
        