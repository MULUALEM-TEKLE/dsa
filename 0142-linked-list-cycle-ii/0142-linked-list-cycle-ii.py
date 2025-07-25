# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head : return None
        fast = slow = head 

        while fast and fast.next : 
            fast = fast.next.next 
            slow = slow.next 
            if slow == fast : 
                break 
        
        if not fast or not fast.next : 
            return None
        
        slow2 = head 
        while True : 
            if slow == slow2 : return slow2
            slow2 = slow2.next 
            slow = slow.next 
        
        return slow2