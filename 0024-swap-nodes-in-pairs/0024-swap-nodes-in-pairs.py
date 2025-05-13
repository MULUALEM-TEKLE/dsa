# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def print_list(head) : 
    cur = head
    l = ""
    while cur : 
        l += f"{cur.val} -> "
        cur = cur.next
    print(l)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        
        prev = dummy
        cur = head

        while cur and cur.next : 
            next_pair = cur.next.next
            second = cur.next

            second.next = cur
            cur.next = next_pair
            prev.next = second

            prev = cur
            cur = next_pair


        return dummy.next

        