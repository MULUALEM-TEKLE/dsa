class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket = {}

        for i , n in enumerate(nums) : 
            bucket_index = n // (valueDiff+1)
            if bucket_index in bucket and abs(n - bucket[bucket_index]) <= valueDiff : 
                return True 
            if bucket_index+1 in bucket and abs(n - bucket[bucket_index+1]) <= valueDiff : 
                return True 
            if bucket_index-1 in bucket and abs(n - bucket[bucket_index-1]) <= valueDiff : 
                return True 

            bucket[bucket_index] = n
            
            if i >= indexDiff : 
                bucket.pop(nums[i-indexDiff]//(valueDiff+1))
        return False