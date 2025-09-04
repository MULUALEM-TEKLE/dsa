class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_ptr = 1
        for right_ptr in range(1, len(nums)):
            if nums[right_ptr] != nums[right_ptr-1]:
                nums[left_ptr]  = nums[right_ptr]
                left_ptr += 1

        print(nums)
        return left_ptr