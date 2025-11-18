
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp , value])
        # print(self.map[key])
       
    def get(self, key: str, timestamp: int) -> str:
        cur = self.map[key]
        res = ""
        low , high = 0, len(cur)-1
        # print(f"getting for timestamp:{timestamp}")
        while low <= high : 
            mid = (low+high)//2
            if cur[mid][0] <= timestamp : 
                res = cur[mid][1]
                low = mid + 1 
            else : 
                high = mid - 1 
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)