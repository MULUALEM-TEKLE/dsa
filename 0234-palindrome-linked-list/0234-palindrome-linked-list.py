# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def print_list(head): 
    s = ""
    while head : 
        s += f"{head.val} ->"
        head = head.next
    print(s[:-2])

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next : 
            fast = fast.next.next
            slow = slow.next
        
        second_half = None
        cur = slow

        while cur : 
            next_node = cur.next
            cur.next = second_half
            second_half = cur
            cur = next_node

        first_half = head
        while second_half : 
            if first_half.val != second_half.val : 
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    
        
