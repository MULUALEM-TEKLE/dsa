class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        courses = prerequisites

        adj = defaultdict(list)

        for a , b in courses : 
            adj[a].append(b)
        
        visited = set()
        visiting = set()

        topsort = []

        def dfs(i) : 
            if i in visiting : 
                return False 
            if i in visited : 
                return True 
            
            visited.add(i)
            visiting.add(i)

            for nei in adj[i] : 
                if not dfs(nei) : 
                    return False 
            
            visiting.remove(i)
            topsort.append(i)
            return True 

        for i in range(n) : 
            if not dfs(i) : 
                return []
        # topsort.reverse()
        return topsort

        


