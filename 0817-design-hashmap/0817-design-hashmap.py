class Pair : 
    def __init__(self, key, value) : 
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.map = [[] for _ in range(self.capacity)]
    
    def hash(self, key) : 
        return key % self.capacity
    
    def rehash(self) : 
        self.capacity = 2 * self.capacity
        newMap = [[] for _ in range(self.capacity)]
       
        oldMap = self.map 
        self.map = newMap 
        self.size = 0
        for chain in oldMap : 
        
            for pair in chain : 
                
                    self.put(pair.key, pair.value)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        chain = self.map[index]

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
        chain = self.map[index]

        for pair in chain : 
            if pair and pair.key == key : 
                return pair.value
        
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        chain = self.map[index]

        for index, pair in enumerate(chain) : 
            if pair and pair.key == key : 
                del chain[index] 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)