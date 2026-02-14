# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find the center
        fast = head
        slow = head

        while fast and fast.next : 
            fast = fast.next.next 
            slow = slow .next 
        
        # reverse the second half
        middle = slow 
        left = None 

        while middle : 
            nxt = middle.next 
            middle.next = left 
            left = middle
            middle = nxt

        second_half = left
        # add the two linked lists in order and find the max
        res = 0
        while head and second_half : 
            res = max(res , head.val + second_half.val)
            head = head.next 
            second_half = second_half.next 

        return res 