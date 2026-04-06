class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for cur in asteroids : 
            while stack and cur < 0 and stack[-1] > 0 : 
                if stack[-1] < abs(cur) : 
                    stack.pop()
                    continue 
                elif stack[-1] == abs(cur) : 
                    stack.pop()
                break
            else : 
                stack.append(cur)
        
        return stack