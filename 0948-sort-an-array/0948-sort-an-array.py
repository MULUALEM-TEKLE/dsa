def merge(nums , start , mid ,  end ) : 
    L = nums[start : mid + 1]
    R = nums[mid + 1  : end + 1]

    LP = RP = 0 
    NP = start

    while LP < len(L) and RP < len(R) : 
        if L[LP] <= R[RP] : 
            nums[NP] = L[LP]
            LP += 1 
        else : 
            nums[NP] = R[RP]
            RP += 1
        NP += 1 
    
    while LP < len(L) : 
        nums[NP] = L[LP]
        LP += 1 
        NP += 1 

    while RP < len(R) : 
        nums[NP] = R[RP]
        RP += 1 
        NP += 1 
    

class Solution:
    def sort_helper(self , nums , start , end) : 
        if start >= end : 
            return 

        mid = (start + end) //2

        self.sort_helper(nums , start , mid)
        self.sort_helper(nums , mid + 1 , end)

        merge(nums , start , mid , end)

    def sortArray(self, nums: List[int]) -> List[int]:

        self.sort_helper(nums , 0 , len(nums) -1 )
        return nums

