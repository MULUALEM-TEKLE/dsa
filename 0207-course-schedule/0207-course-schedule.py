class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisites

        for a,b in courses : 
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        
        states = [UNVISITED] * numCourses

        def dfs(node) : 
            if states[node] == VISITED : return True 
            if states[node] == VISITING : return False
            states[node] = VISITING
            for n in g[node] : 
                if not dfs(n) : return False
            states[node] = VISITED
            return True 
        
        for i in range(numCourses) : 
            if not dfs(i) : return False
        return True
             
            
