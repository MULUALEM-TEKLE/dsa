# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head , head 
        while fast and fast.next : 
            fast = fast.next.next
            slow = slow.next 
        
        shalf = slow
        prev = None 
        while shalf : 
            nxt = shalf.next 
            shalf.next = prev 
            prev = shalf
            shalf = nxt

        rhead = prev

        maxsum = 0
        while rhead : 
            if (cursum:=rhead.val+head.val) > maxsum : 
                maxsum = cursum
            # maxsum = max(maxsum , rhead.val+head.val)
            rhead , head = rhead.next , head.next 
        
        return maxsum
        
