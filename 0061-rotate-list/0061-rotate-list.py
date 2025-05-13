# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        
        length = 1 
        c = head
        while c.next : 
            length += 1
            c = c.next
        print(f"te list length is {length} ")

        dummy = ListNode(0, head)
        
        fast = dummy.next
        counter = 1
        effective_rotation = k % length
        while counter <= effective_rotation : 
            if fast.next.next == None:
                tmp = dummy.next
                dummy.next = fast.next
                dummy.next.next = tmp
                fast.next = None
                counter += 1
                fast = dummy.next
                # continue
            else : 
                fast = fast.next
        
        return dummy.next


        