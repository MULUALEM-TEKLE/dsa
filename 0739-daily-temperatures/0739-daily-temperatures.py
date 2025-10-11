class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = []
        ans = [0] * len(temp)

        for i,t in enumerate(temp) : 
            while stack and stack[-1][0] < temp[i] : 
                _ , stack_i = stack.pop()
                ans[stack_i] = i - stack_i 
            stack.append((t , i))           
        
        return ans
