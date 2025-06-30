class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        
        for index , num in enumerate(nums) : 
            if index > 0 and num == nums[index - 1]: 
                continue
            
            left, right = index + 1 , len(nums) -1 

            while left < right : 
                if num + nums[left] + nums[right] > 0 : 
                    right -= 1 
                elif num + nums[left] + nums[right] < 0 :
                    left += 1  
                else : 
                    res = (nums[left], nums[right], num)
                    output.add(res)
                    left += 1 
                    right -= 1 
                    # while nums[left] == nums[left - 1 ] and left < right : 
                    #     left += 1 
        return list(output)