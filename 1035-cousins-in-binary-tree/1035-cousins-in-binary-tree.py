# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([[root , 0 , None]])
        depth = 0
        data = []
        while q : 
            for _ in range(len(q)) : 
                node , dep , par = q.popleft()
                if node.val == x or node.val == y : 
                    data.append([dep , par])
                if node.left : 
                    q.append([node.left , dep+1 , node.val])
                if node.right : 
                    q.append([node.right , dep+1 , node.val])

        return data[0][0] == data[1][0] and data[0][1] != data[1][1] 
        
            