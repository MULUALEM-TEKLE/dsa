class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low , high = 0 , len(matrix) -1
        while low <= high:
            mid = (low + high)//2
            if target == matrix[mid][0] or  matrix[mid][-1] == target :
                return True
            elif target > matrix[mid][0] and  matrix[mid][-1] > target : 
                break
            elif target < matrix[mid][0] : 
                high = mid -1
            else : 
               low = mid + 1

        location = matrix[((high+ low)//2)]
        low , high = 0 , len(location) -1
        while low <= high:
            mid = (low + high)//2
            print(f"mid is now {mid}")
            if target > location[mid] : 
                low = mid + 1
            elif target < location[mid] : 
                high = mid -1
            else : 
               return True

        return False