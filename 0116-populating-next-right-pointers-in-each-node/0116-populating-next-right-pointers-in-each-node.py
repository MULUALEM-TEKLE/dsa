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
            return

        q = deque([root])
        level = 0

        while q : 
            print(f"on level : {level}")
            if level == 0 : 
                q[0].next = None
            else : 
                for i in range(0 , len(q)-1 ) : 
                    # print(q[i-1])
                    q[i].next = q[i + 1]

            for _ in range(len(q)) : 
                node = q.popleft()
                print(node.val)
                if node.left and node.right: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return root