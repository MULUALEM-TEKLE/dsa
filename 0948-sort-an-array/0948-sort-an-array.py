def merge(nums , start , mid , end) : 
    # copy left and right arrays
    L = nums[start : mid + 1 ]
    R = nums[mid + 1 : end + 1 ]
    # instantiate pointers
    LP = RP = 0
    AP = start
    # compare and merge from left and right
    while LP < len(L) and RP < len(R) : 
        if L[LP] < R[RP] : 
            nums[AP] = L[LP]
            LP += 1 
        else : 
            nums[AP] = R[RP]
            RP += 1 
        AP += 1
    # merge what is left from the right and left arrays
    while LP < len(L) : 
        nums[AP] = L[LP]
        LP += 1 
        AP += 1

    while RP < len(R) : 
        nums[AP] = R[RP]
        RP += 1 
        AP += 1

class Solution:
    def sort_helper(self ,nums , start , end) : 
        # define base conditions
        if start >= end :
            return  
        # find the mid 
        mid = start + (end - start)//2
        # do the recursive calls
        self.sort_helper(nums , start , mid)
        self.sort_helper(nums ,mid + 1 , end)
        # merge left and right halves
        merge(nums , start , mid , end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort_helper(nums , 0 , len(nums) -1 )
        return nums