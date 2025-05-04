# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        temp_arr = []
        
        while cur : 
            temp_arr.append(cur.val)
            cur = cur.next
        
        print(temp_arr)

        
       
        if len(temp_arr) == 0 : return 
        temp_arr.reverse()
        new_head = ListNode(temp_arr[0])
        curr = new_head
        for i in range(1, len(temp_arr)):
            print("adding : " , temp_arr[i])
            new_node = ListNode(temp_arr[i])
            curr.next = new_node
            # print(new_head)
            curr = curr.next

        print(new_head)

        return new_head

        