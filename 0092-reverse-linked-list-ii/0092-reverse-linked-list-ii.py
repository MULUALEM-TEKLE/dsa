# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)

        lp , cur = dummy , head
        for _ in range(left-1) : 
            lp , cur = lp.next , cur.next
        
        prev = None 
        for _ in range(right-left+1) : 
            nxt = cur.next 
            cur.next = prev 
            prev , cur = cur , nxt
        
        lp.next.next = cur
        lp.next = prev

        return dummy.next
