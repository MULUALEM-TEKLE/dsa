# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Cousin : 
    def __init__(self , parent , depth) : 
        self.parent = parent
        self.depth = depth
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def bfs(root) : 
            q = deque([[root , 0 , None]])
            candidates = []
            while q : 
                for _ in range(len(q)) : 
                    node, depth , parent = q.popleft()
                    if node.val == x or node.val == y : 
                        candidates.append(Cousin(parent.val if parent else None, depth)) 
                            
                    if node.right : 
                        q.append([node.right , depth+1 , node])
                    if node.left : 
                        q.append([node.left , depth+1 , node])
            print(candidates[0].parent)
            print(candidates[1].parent)
            return candidates[0].parent != candidates[1].parent and candidates[0].depth == candidates[1].depth

        return bfs(root)