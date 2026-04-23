class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital , profits))

        av_profits = []
        current_project_idx = 0 
        n = len(projects)


        for _ in range(k) : 
            while current_project_idx < n and projects[current_project_idx][0] <= w : 
                heapq.heappush(av_profits , -projects[current_project_idx][1])
                current_project_idx += 1 
            
            if not av_profits : 
                break 
            
            w += -heapq.heappop(av_profits)
        
        return w