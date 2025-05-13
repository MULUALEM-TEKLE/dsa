# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        length = 1
        cur = head
        while cur.next : 
            length += 1
            cur = cur.next
        
        if length == 1 and n == 1 : 
            head = None
            return head

        print(f"length of list is {length}")
        print(f"and target element is at {length - n + 1}")
        target_pos = length - n + 1
        starting_pos = 1

        if target_pos == 1 : 
            head = head.next
            return head

        while right.next and starting_pos < target_pos  : 
            left = right
            right = right.next
            starting_pos += 1 
        
        left.next = right.next
        print(head)
        
        print(right.val)
        print(left.val)

        return head
        