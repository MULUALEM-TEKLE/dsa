"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root : 
            return []
        
        res = []
        q = deque([root])

        while q : 
            tmp = []
            for _ in range(len(q)) : 
                node = q.popleft()
                tmp.append(node.val)
                # if children : 
                for child in node.children : 
                    q.append(child)
            res.append(tmp)
        
        return res