class DetectSquares:

    def __init__(self):
        self.points_counter = Counter()
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points_counter[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0 
        px , py = point 

        for x , y in self.points : 
            if abs(px-x) != abs(py-y) or x == px or y == py : 
                continue 
            res += self.points_counter[(x , py)] * self.points_counter[((px , y))]
        
        return res 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)