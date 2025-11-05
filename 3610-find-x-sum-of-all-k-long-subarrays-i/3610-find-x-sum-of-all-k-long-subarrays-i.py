from heapq import heappush, heappop


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        def process(arr):
            cnt = Counter(arr)
            pq = []
            for key, val in cnt.items():
                heappush(pq, [val, key])
                if len(pq) > x:
                    heappop(pq)
            summ = 0
            for m,n in pq:
                summ += m*n

            res.append(summ)

        for left in range(len(nums) - k + 1):
            process(nums[left : left + k])

        return res
