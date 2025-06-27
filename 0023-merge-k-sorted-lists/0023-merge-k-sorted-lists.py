# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy 

        while list1 and list2 : 
            if list1.val < list2.val : 
                cur.next = list1
                list1 = list1.next 
            else : 
                cur.next = list2
                list2 = list2.next
            cur = cur.next 
        
        if list1 : 
            cur.next = list1
        
        if list2 : 
            cur.next = list2
        
        return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 : 
            return None 
        elif len(lists) == 1 : 
            return lists[0]
        else : 
            output = lists[0]

            for i in range(1 , len(lists)) : 
                output = mergeTwoLists(output , lists[i])
            return output