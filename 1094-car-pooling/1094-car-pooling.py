class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x : x[1])

        departures = []
        current_load = 0 

        for num , start , end in trips : 
            while departures and departures[0][0] <= start : 
                _ , num_ = heapq.heappop(departures)
                current_load -= num_
            
            current_load += num 
            heapq.heappush(departures , [end , num])

            if current_load > capacity : return False 
        
        return True