class Node : 
    def __init__(self, key=None , val=None , prev=None, next=None) : 
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()

        self.left.next , self.right.prev = self.right , self.left
    
    def remove(self, node) : 
        # connect the node prev to this node and the next node of current node
        node.prev.next = node.next 
        node.next.prev = node.prev
    
    def insert(self, node) : 
        # here we gotta insert at the right end, since whatever we insert should always be 
        # MRU so at the right end we insert the current node with the correct pointer update
        MRU = self.right.prev 
        MRU.next = node
        node.prev = MRU
        node.next = self.right
        self.right.prev = node
        

    def get(self, key: int) -> int:
        # we gotta check on the cache, if so return the val, and remove and insert the node so it becomes the MRU
        if key in self.cache : 
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

        

    def put(self, key: int, value: int) -> None:
        # first check if the node is in our cache, if so we just update its value, if not we check if our capacity is full if so remove MRU and add the node at the MRU end
        if key in self.cache : 
            node = self.cache[key]
            node.val = value 
            self.remove(node)
            self.insert(node)
        else : 
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.cap : 
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)