class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(start , mid , end) : 
            L = nums[start : mid+1]
            R = nums[mid+1 : end+1]
            LP = RP = 0
            NP = start

            while LP < len(L) and RP < len(R) : 
                if L[LP] < R[RP] : 
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

        def m_sort(start , end) : 
            if end - start + 1 <= 1 : 
                return 
            mid = (start+end) // 2 
            m_sort(start , mid)
            m_sort(mid+1 , end)

            merge(start , mid , end)

            return nums
        
        return m_sort(0 , len(nums))


        