"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : return
        o2n = {}

        cur = head 
        while cur : 
            o2n[cur] = Node(cur.val)
            cur = cur.next 
        
        cur = head
        while cur : 
            node = o2n[cur]
            node.next = o2n[cur.next] if cur.next else None 
            node.random = o2n[cur.random] if cur.random else None 
            cur = cur.next 
        
        return o2n[head]