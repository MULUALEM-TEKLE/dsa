class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s_nums = sorted(nums)
        table = defaultdict(list)

        for i , num in enumerate(nums) : 
            table[num].append(i)
        
        low , high = 0 , len(nums)-1 

        while low < high : 
            if s_nums[low] + s_nums[high] > target : 
                high -= 1
            elif s_nums[low] + s_nums[high] < target : 
                low += 1 
            else : 
                if s_nums[low] == s_nums[high] : 
                    return table[s_nums[low]]
                return [table[s_nums[low]][0] , table[s_nums[high]][0]]