class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums2) == 0 : 
            return nums1

        repl_ctr = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and repl_ctr < n :
                nums1[i] = nums2[repl_ctr]
                repl_ctr += 1 

        for i in range(len(nums1)):
            j = i 
            while j > 0 and nums1[j] < nums1[j-1] : 
                nums1[j],  nums1[j-1] = nums1[j-1], nums1[j]
                j -= 1
        