class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        if k == 0 : 
            return False
        for i in range(min(len(nums), k)) : 
            if nums[i] in window : 
                return True 
            window.add(nums[i])
        left = 0
        for right in range(k , len(nums)) : 
            if nums[right] in window : 
                return True
            window.remove(nums[left])
            window.add(nums[right])
            left += 1
        return False