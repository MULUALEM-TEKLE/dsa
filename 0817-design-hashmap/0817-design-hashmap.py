class Pair : 
    def __init__(self, key, value) : 
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.buckets = [[] for _ in range(self.capacity)]
    
    def hash(self, key) : 
        return key % self.capacity
    
    def rehash(self) : 
        # print(f"Rehashing from capacity {self.capacity} to {2 * self.capacity}")
        self.capacity *= 2 # Double the capacity
        new_buckets = [[] for _ in range(self.capacity)] # New bucket array
       
        old_buckets = self.buckets # Keep a reference to the old buckets
        self.buckets = new_buckets # Update self.buckets to the new array
        self.size = 0 # Reset size, will be re-counted by put operations

        # Re-insert all existing key-value pairs into the new, larger map
        for chain in old_buckets:
            for pair in chain:
                # Use the existing put method to correctly re-hash and insert
                self.put(pair.key, pair.value) 

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]

        for i, pair in enumerate(chain) : 
            if pair and pair.key == key : 
                chain[i].value = value
                return 
        
        chain.append(Pair(key, value))
        self.size += 1 

        if self.size >= self.capacity // 2 : 
            self.rehash()
       
    def get(self, key: int) -> int:
        index = self.hash(key)
        chain = self.buckets[index]

        for pair in chain : 
            if pair and pair.key == key : 
                return pair.value
        
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]

        for index, pair in enumerate(chain) : 
            if pair and pair.key == key : 
                del chain[index] 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)