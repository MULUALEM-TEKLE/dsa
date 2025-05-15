# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        first = ListNode()
        f = first

        second = ListNode()
        s = second

        cur = head

        while cur  : 
            if cur.val < x:
                f.next = cur
                f = f.next
            else : 
                s.next = cur
                s= s.next

            cur = cur.next
        
        s.next = None
        f.next = second.next
        
        return first.next
        