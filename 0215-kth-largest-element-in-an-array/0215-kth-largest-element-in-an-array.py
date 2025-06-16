class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [num * -1 for num in nums]
        heapq.heapify(heap)


        while k > 1 : 
            heapq.heappop(heap)
            k -= 1
        
        return (heap[0] * -1)