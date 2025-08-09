class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0 
        s = set()
        s.add(nums[left])
        for right in range(1 , len(nums)) : 
            if (right - left ) > k : 
                s.remove(nums[left])
                left += 1 
                
            if nums[right] in s : return True 
            s.add(nums[right])
        return False

            