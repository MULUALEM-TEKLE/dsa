# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root) : 
            q = deque([root])
            level = 0

            while q : 
                tmp = []
                nodes = []
                for _ in range(len(q)) : 
                    node = q.popleft()
                    tmp.append(node.val)
                    nodes.append(node)
                    if node.left : q.append(node.left)
                    if node.right : q.append(node.right)
                
                if level % 2 != 0 : 
                    tmp.reverse()
                    for index , node in enumerate(nodes) : 
                        node.val = tmp[index]
                level += 1 
                
        bfs(root)

        return root 
