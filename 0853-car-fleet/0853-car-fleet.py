class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - position)/speed for position  , speed in sorted(zip(position , speed))]

        current_time , result = 0 , 0

        for t in time[::-1] : 
            if t > current_time : 
                result += 1 
                current_time = t 
        
        return result
            