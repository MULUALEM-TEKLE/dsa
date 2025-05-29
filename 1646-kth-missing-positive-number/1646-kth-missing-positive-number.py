class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = k
        for i in range(1 , max(arr) + k + 1 ) : 
            if i not in arr : 
                count -= 1 
                if count == 0 : 
                    return i