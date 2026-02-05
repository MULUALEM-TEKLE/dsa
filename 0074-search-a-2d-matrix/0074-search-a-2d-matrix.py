class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix) , len(matrix[0])
        low , high = 0 , row-1
        location = -1

        while low <= high : 
            mid = (low+high)//2
            if matrix[mid][0] > target : 
                high = mid - 1 
            else : 
                low = mid + 1 
                location = mid 
        
        low , high = 0 , col-1

        while low <= high : 
            mid = (low+high)//2
            if matrix[location][mid] < target :
                low = mid + 1 
            elif matrix[location][mid] > target : 
                high = mid -1 
            else : 
                return True 
        
        return False 
        
        