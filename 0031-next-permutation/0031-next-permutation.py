class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find our pivot 
        pivot = -1
        n = len(nums)
        for i in range(n-1 , -1 , -1) : 
            if nums[i-1] < nums[i] : 
                pivot = i-1
                break
        
        print(f"pivot > {pivot}")

        if pivot == -1 : 
            nums.reverse()
            return

        swap = n-1

        while nums[pivot] >= nums[swap] : 
            swap -= 1 
        
        nums[pivot] , nums[swap] = nums[swap] , nums[pivot]

        nums[pivot+1 : ] = reversed(nums[pivot+1 : ])


        

