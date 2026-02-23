class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def get_prefix(nums) : 
            stack = []
            done = False 

            for num in nums : 
                if stack and stack[-1] > num : 
                    done = True 

                if done : 
                    while stack and stack[-1] > num : 
                        stack.pop()
                else : 
                    stack.append(num) 

            return len(stack)

        prefix = get_prefix(nums)

        if prefix == len(nums) : 
            return 0 

        rev_nums = [-x for x in nums[::-1]]
        print(rev_nums)
        suffix = get_prefix(rev_nums)

        return len(nums) - suffix - prefix       