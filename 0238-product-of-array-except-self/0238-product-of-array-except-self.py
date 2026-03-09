class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_counter = Counter(nums)
        n = len(nums)
        res = [0] * n
        if 0 in num_counter : 
            if num_counter[0] == 1 : 
                prod = 1 
                for num in nums : 
                    if num == 0 : 
                        continue 
                    else : 
                        prod *= num 

                for i in range(len(nums)) : 
                    if nums[i] == 0 : 
                        res[i] = prod
                return res 
            else :
                return res
        else : 
            prod = 1 
            for num in nums : 
                prod *= num
            return [int(prod/num) for num in nums ]