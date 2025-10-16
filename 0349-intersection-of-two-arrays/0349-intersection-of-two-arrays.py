class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # s_nums1 = set(nums1)
        # s_nums2 = set(nums2)

        res = set()

        for num in nums1 + nums2 : 
            if num in nums1 and num in nums2 : 
                res.add(num)
        
        return list(res)