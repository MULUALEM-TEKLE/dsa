class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [[enq , pro , idx] for idx , (enq , pro) in enumerate(tasks) ]

        indexed_tasks.sort()

        res = []
        min_heap = []
        cur_time = 0 
        task_idx = 0 
        n = len(tasks)

        while task_idx < n or min_heap : 
            if not min_heap and cur_time < indexed_tasks[task_idx][0] : 
                cur_time = indexed_tasks[task_idx][0]
            
            while task_idx < n and indexed_tasks[task_idx][0] <= cur_time :
                enq , pro , idx = indexed_tasks[task_idx]
                heapq.heappush(min_heap , [pro , idx])
                task_idx += 1 
            
            pro_time , original_idx = heapq.heappop(min_heap)
            cur_time += pro_time
            res.append(original_idx)
        
        return res 
