# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_group_end = head 
        group_size = 2 

        while prev_group_end.next : 
            cur = prev_group_end.next 
            count = 0 
            while count < group_size and cur : 
                count += 1
                cur = cur.next 
            
            if count % 2 == 0 : 
                cur = prev_group_end.next 
                reverse_prev = None 
                for _ in range(count) : 
                    nxt = cur.next 
                    cur.next = reverse_prev 
                    reverse_prev = cur 
                    cur = nxt 

                group_start = prev_group_end.next 
                prev_group_end.next = reverse_prev
                group_start.next = cur 
                prev_group_end = group_start 
            else : 
                for _ in range(count) : 
                    prev_group_end = prev_group_end.next 
                    
            group_size += 1 
        
        return head