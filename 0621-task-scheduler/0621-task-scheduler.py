from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        interval = 0 
        pq = []
        q = deque()
        for key, val in Counter(tasks).items() : 
           heappush(pq , -val) 
        while pq or q : 
            interval += 1
            if pq : 
                cur = heappop(pq)
                cur += 1 
                if cur : q.append((cur , interval+n)) 
            if q and q[0][1] == interval : 
                heappush(pq , q.popleft()[0])
        return interval

        