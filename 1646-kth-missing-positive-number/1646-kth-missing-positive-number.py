class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # for i in range(1 , max(arr) + k + 1 ) : 
        #     if i not in arr and  : 
        #         k -= 1 
        #         if k == 0 : 
        #             return i

        low , high = 0 , len(arr) 

        while low < high : 
            mid = (low + high)//2

            if (arr[mid] - mid - 1) < k : 
                low = mid + 1 
            else : 
                high = mid
        
        return low + k

'''
[2,3,4,7,11]
 0 1 2 3  4
'''