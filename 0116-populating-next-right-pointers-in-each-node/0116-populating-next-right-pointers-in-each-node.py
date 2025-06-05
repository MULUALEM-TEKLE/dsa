"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root : 
            return root

        q = deque([root])

        while q : 
            tmp = []
            for _ in range(len(q)) : 
                node = q.popleft()
                tmp.append(node)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)

            for i in range(1 , len(q)) : 
                q[i-1].next = q[i]

        return root 