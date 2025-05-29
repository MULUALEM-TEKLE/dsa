# class Solution:
#     def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
#         def binary_search(array , target) : 
#             low , high = 0 , len(array) - 1
            
#             while low <= high : 
#                 mid = (low + high ) // 2

#                 if array[mid] < target : 
#                     low = mid + 1
#                 elif array[mid] > target : 
#                     high = mid - 1
#                 else : 
#                     return True

#             return False 

#         min_list = nums1
#         max_list = nums2
#         if len(nums2) < len(nums1) : 
#             min_list = nums2
#             max_list = nums1
        
#         min_list = list(set(min_list))
#         min_list.sort()
       
      
     

#         for i in range(len(min_list)) :
#             if binary_search(max_list , min_list[i]) : 
#                 return min_list[i]

#         return -1 

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums2[j] < nums1[i]:
                j+=1
            else:
                return nums1[i]
        return -1


