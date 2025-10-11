class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = []
        ans = [0] * len(temp)

        for i,t in enumerate(temp) : 
            while stack and temp[stack[-1]] < temp[i] : 
                stack_i = stack.pop()
                ans[stack_i] = i - stack_i 
            stack.append(i)           
        
        return ans
