class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        courses = prerequisites
        adj = defaultdict(list)

        for src , dst in courses : 
            adj[src].append(dst)
        
        VISITING = 1
        VISITED = 2
        UNVISITED = 0 

        state = [0] * n

        def dfs(i) : 
            if state[i] == VISITING : 
                return False 
            if state[i] == VISITED : 
                return True
            
            state[i] = VISITING
            
            for nei in adj[i] : 
                if not dfs(nei) : 
                    return False 
            
            state[i] = VISITED
            return True
        
        for i in range(n) : 
            if not dfs(i) : 
                return False
        
        return True 

       
        
        

        