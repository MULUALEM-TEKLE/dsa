class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001

        for num , start , end in trips : 
            stops[start] += num 
            stops[end] -= num

        current_passengers = 0 
        for change in stops : 
            current_passengers += change 
            if current_passengers > capacity : return False 

        return True  