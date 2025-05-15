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
            print(f"current val : {cur.val}")
            if cur.val < x:
                f.next = ListNode(cur.val)
                f = f.next
            else : 
                s.next = ListNode(cur.val)
                s= s.next

            cur = cur.next
        
        f.next = second.next
        # print(first)
        # print(second)

        return first.next
        