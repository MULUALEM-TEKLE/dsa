class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        left , right = matrix[0][0] , matrix[n-1][n-1]

        while left < right : 
            mid = (left+right)//2
            count = 0

            for i in range(n) : 
                for j in range(n) : 
                    if matrix[i][j] <= mid : 
                        count += 1 

            if count < k : 
                left = mid + 1 
            else : 
                right = mid

        return left 