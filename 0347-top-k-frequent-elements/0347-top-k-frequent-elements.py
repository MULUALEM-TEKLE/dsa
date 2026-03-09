import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        heap = []
        for num, count in nums_counter.items() : 
            heapq.heappush(heap , (-1*count , num))

        res = []
        while k > 0 :  
            _ , top = heapq.heappop(heap)
            res.append(top)
            k -= 1 
        
        return res 

