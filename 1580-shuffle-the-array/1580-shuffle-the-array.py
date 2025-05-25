class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i , right in enumerate(range(n, len(nums))):
            if i == n : 
                return
            result.append(nums[i])
            result.append(nums[right])
        return result

        