class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = prerequisites
        N = numCourses

        matrix = [[False] * N for _ in range(N)]

        for pre , course in courses : 
            matrix[pre][course] = True
        

        
        for k in range(N) : 
            for i in range(N) : 
                for j in range(N) : 
                    if matrix[i][k] and matrix[k][j] : 
                        matrix[i][j] = True 
        
        res = []
        for pre , course in queries : 
            res.append(matrix[pre][course])
        
        return res
