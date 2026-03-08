class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = Counter({0:1})
        # prefix_sums[0] = 1
        total = count = 0 
        for num in nums : 
            total += num
            target = total-k 
            if target in prefix_sums : 
                count += prefix_sums[target]
            prefix_sums[total] += 1

        return count  
            
