class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        for num in nums : 
            if num_count[num] > 1 : 
                return True
        return False