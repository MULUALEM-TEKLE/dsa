class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first lets find on which row the target might reside in
        low , high = 0 , len(matrix) -1
        mid = None
        while low <= high:
            mid = (low + high)//2
            print(f"mid is now {mid}")
            if target > matrix[mid][0] : 
                print(f"since target > {matrix[mid][0]} ")
                low = mid + 1
                print(f"low is now {low}")
            elif target < matrix[mid][0] : 
                print(f"since target < {matrix[mid][0]} ")
                high = mid -1
                print(f"high is now {high}")
            else : 
               return True

        location = matrix[high]
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
       

        # low , high = 0 , len(matrix[location]) -1


        # after zooming in like that we might search inside the specific row 
        