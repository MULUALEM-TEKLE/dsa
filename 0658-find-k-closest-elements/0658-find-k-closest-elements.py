class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left , right = 0 , len(arr)-1

        while right-left + 1 > k : 
            left_distance = abs(x-arr[left])
            right_distance = abs(x-arr[right])

            if left_distance > right_distance : 
                left += 1 
            else : 
                right -= 1
        
        return arr[left : right+1]