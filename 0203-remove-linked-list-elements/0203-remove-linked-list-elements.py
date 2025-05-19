# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        ptr = head

        while ptr : 
            if ptr.val != val : 
                cur.next = ListNode(ptr.val)
                cur = cur.next
                ptr = ptr.next
            else : 
                ptr = ptr.next 

            
        
        return dummy.next