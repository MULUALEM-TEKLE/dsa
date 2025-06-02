# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root : return []

        q = deque([[root, None]])
        level = 0

        while q : 
            tmp = {}
            for _ in range(len(q)) : 
                node , parent = q.popleft()
                tmp[node.val] = parent
                if node.left : 
                    q.append([node.left , node])
                if node.right : 
                    q.append([node.right , node])

            if  x in tmp.keys() and y in tmp.keys() and tmp[x] != tmp[y]  : 
                return True

            level += 1 

        return False