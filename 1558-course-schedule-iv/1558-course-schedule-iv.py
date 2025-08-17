class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = prerequisites
        N = numCourses

        is_pre = [[False] * N for _ in range(N)]

        for course , pre in courses : 
            is_pre[course][pre] = True

        for via in range(N) : 
            for start in range(N) : 
                for end in range(N) : 
                    if is_pre[start][via] and is_pre[via][end] : 
                        is_pre[start][end] = True

        res = []
        for u , v in queries : 
            res.append(is_pre[u][v])
        
        return res 
