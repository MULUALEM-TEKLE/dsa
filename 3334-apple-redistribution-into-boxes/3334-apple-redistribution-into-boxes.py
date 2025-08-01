class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)

        total_apples = sum(apple)

        res = 0
        for cap in capacity : 
            total_apples -= cap
            res += 1 
            if total_apples <= 0 : 
                return res 