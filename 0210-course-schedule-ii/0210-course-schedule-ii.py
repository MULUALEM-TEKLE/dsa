class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = prerequisites
        adj = defaultdict(list)

        for course , pre in courses : 
            adj[course].append(pre)
        
        tsort = []
        visited = set()
        visiting = set()

        def dfs(course) : 
            if course in visiting : 
                return False 
            if course in visited : 
                return True 

            visiting.add(course)
            
            for neighbor in adj[course] : 
                if not dfs(neighbor) : 
                    return False

            visited.add(course)
            tsort.append(course)
            visiting.remove(course)

            return True

        for course in range(numCourses) : 
            if course not in visited : 
                if not dfs(course) : return []
        
        return tsort