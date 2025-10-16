class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # s_nums1 = set(nums1)
        # s_nums2 = set(nums2)
        seen = set(nums1)
        res = []

        for num in nums2 : 
            if num in seen: 
                res.append(num)
                seen.remove(num)
        
        return res