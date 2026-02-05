def merge(arr ,start , mid , end) : 
    L = arr[start : mid + 1]
    R = arr[mid + 1 : end + 1]
    LP = RP = 0
    AP = start 

    while LP < len(L) and RP < len(R) : 
        if R[RP] < L[LP] : 
            arr[AP] = R[RP]
            RP += 1 
        else : 
            arr[AP] = L[LP]
            LP += 1 
        AP += 1 
    
    while LP < len(L) : 
        arr[AP] = L[LP]
        LP += 1 
        AP += 1 
    while RP < len(R) : 
        arr[AP] = R[RP]
        RP += 1 
        AP += 1 
    
def sort(arr , start , end) : 
    if end - start + 1 <= 1 : 
        return 
    
    mid = (start + end )//2

    sort(arr , start , mid)
    sort(arr , mid + 1 , end)

    merge(arr , start , mid , end)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sort(nums , 0 , len(nums)-1)
        return nums