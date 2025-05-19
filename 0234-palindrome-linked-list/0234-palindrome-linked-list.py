# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next : 
            fast = fast.next.next
            slow = slow.next
        
        second_half = None

        while slow : 
            next_node = slow.next
            slow.next = second_half
            second_half = slow
            slow = next_node

        
        while second_half : 
            if head.val != second_half.val : 
                return False
            head = head.next
            second_half = second_half.next

        return True

    
        
