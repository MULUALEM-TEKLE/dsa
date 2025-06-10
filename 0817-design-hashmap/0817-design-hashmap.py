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
        self.capacity = 2 * self.capacity
        new_buckets = [[] for _ in range(self.capacity)]
       
        old_buckets = self.buckets 
        self.buckets = new_buckets 
        self.size = 0
        for chain in old_buckets : 
            for pair in chain : 
                self.put(pair.key, pair.value)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]

        for i, pair in enumerate(chain) : 
            if pair.key == key : 
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
            if pair.key == key : 
                return pair.value
        
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]

        for index, pair in enumerate(chain) : 
            if pair.key == key : 
                del chain[index] 
                self.size -= 1
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)