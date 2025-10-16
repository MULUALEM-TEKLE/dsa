class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        courses = prerequisites
        adj = defaultdict(list)

        for src , dst in courses : 
            adj[src].append(dst)
        
        visited = set()
        path = set()

        def dfs(i) : 
            if i in path : 
                return False 

            if i in visited : 
                return True 
            
            path.add(i)
            visited.add(i)

            for neighbor in adj[i] : 
                if not dfs(neighbor) : 
                    return False

            path.remove(i)
            return True

        for i in range(n) : 
            if not dfs(i) : 
                return False
        return True
    
       
        
        

        