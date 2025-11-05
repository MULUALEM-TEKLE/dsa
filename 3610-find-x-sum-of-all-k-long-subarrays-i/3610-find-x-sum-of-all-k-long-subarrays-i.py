from heapq import heappush , heappop
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        def process(arr) : 
            cnt = Counter(arr)
            print(cnt)
            pq = []
            for key,val in cnt.items() : 
                heappush(pq , [val , key])
                if len(pq) > x : 
                    heappop(pq)
            # print(pq)
            summ = 0
            for i in range(len(pq)) : 
                summ += pq[i][0] * pq[i][1]
            
            res.append(summ)
            

            
        
        for left in range(len(nums)-k+1) : 
            process(sorted(nums[left:left+k]))


        return res