# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_arr = []
        freq_table = {}
        
        cur = head 
        while cur :
            temp_arr.append(cur.val)
            if cur.val in freq_table.keys():
                freq_table[cur.val] += 1
            else : 
                freq_table[cur.val] = 1
            cur =  cur.next

        dummy = ListNode(1)
        cur = dummy
        for val in sorted([i for i in freq_table.keys() if freq_table[i] ==  1]) : 
            cur.next = ListNode(val)
            cur = cur.next


        return dummy.next

        
        