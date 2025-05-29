class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binary_search(target) : 
            low , high = 0 , len(nums) - 1   
            pos = len(nums)
            while low <= high : 
                mid = (low + high) // 2

                if nums[mid] < target : 
                    low = mid + 1 
                else : 
                    high = mid - 1
                    pos = mid 
            
            return pos

        print(binary_search(0))
        print(binary_search(1))

        return max(len(nums) - binary_search(1) , binary_search(0) )
        
           
