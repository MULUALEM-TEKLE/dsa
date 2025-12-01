class SnapshotArray:

    def __init__(self, length: int):
        self.history = [[[-1 ,0]] for _ in range(length)]
        self.snap_ = 0

    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.snap_ , val])

    def snap(self) -> int:
        self.snap_ += 1 
        return self.snap_ - 1 

    def get(self, index: int, snap_id: int) -> int:
        left , right = 0 , len(self.history[index])-1
        res = -1 
        while left <= right : 
            mid = (left + right)//2
            if self.history[index][mid][0] <= snap_id : 
                res = self.history[index][mid][1] 
                left = mid + 1 
            else : 
                right = mid - 1 
        return res 



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)