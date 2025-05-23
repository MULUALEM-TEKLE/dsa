# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        cur = result

        while l1 and l2 : 
            sum_ = l1.val + l2.val + carry
            print(f"sum is {sum_}")
            if sum_ > 9 : 
                carry = 1
                cur.next = ListNode(sum_ % 10)
            else : 
                carry = 0
                cur.next = ListNode(sum_)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        while l1 : 
            sum_ = l1.val + carry
            print(f"sum is {sum_}")
            if sum_ > 9 : 
                carry = 1
                cur.next = ListNode(sum_ % 10)
            else : 
                carry = 0
                cur.next = ListNode(sum_)
            l1 = l1.next
            cur = cur.next

        while l2 : 
            sum_ = l2.val + carry
            print(f"sum is {sum_}")
            if sum_ > 9 : 
                carry = 1
                cur.next = ListNode(sum_ % 10)
            else : 
                carry = 0
                cur.next = ListNode(sum_)
            l2 = l2.next
            cur = cur.next
        
        if carry : 
            cur.next = ListNode(1)
            
        
        return result.next
        