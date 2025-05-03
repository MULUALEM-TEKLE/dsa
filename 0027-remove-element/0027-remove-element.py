class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_ptr = 0
        for right_ptr in range( len(nums)):
            if nums[right_ptr] != val : 
                nums[left_ptr] = nums[right_ptr]
                left_ptr += 1
                continue
        return left_ptr
            
            
           