class ListNode : 
    def __init__(self , val=None , next=None) : 
        self.val = val 
        self.next = next
class MyHashSet:

    def __init__(self):
        self.capacity = 1000
        self.map = [ListNode(-1) for _ in range(self.capacity)]
    
    def hash(self, key) : 
        return key%self.capacity

    def add(self, key: int) -> None:
        chain = self.map[self.hash(key)]

        while chain.next : 
            if chain.next.val == key : 
                return 
            chain = chain.next
        new_node = ListNode(key)
        chain.next = new_node


    def remove(self, key: int) -> None:
        chain = self.map[self.hash(key)]

        while chain and chain.next : 
            if chain.next.val == key : 
                chain.next = chain.next.next
            chain = chain.next
        

    def contains(self, key: int) -> bool:
        chain = self.map[self.hash(key)]

        while chain.next : 
            if chain.next.val == key : 
                return True 
            chain = chain.next 
        return False 
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)