class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a , b in prerequisites : 
            adj[a].append(b)
        
        visited = set()
        visiting = set()

        def dfs(i) : 
            if i in visiting : 
                return False 
            if i in visited : 
                return True 
            
            visiting.add(i)
            
            for nei in adj[i] : 
                if not dfs(nei) : 
                    return False
            
            visiting.remove(i)
            visited.add(i)
            return True
                
            
        
        for i in range(numCourses) : 
            if not dfs(i) : 
                return False 
        
        return True