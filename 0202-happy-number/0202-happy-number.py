class Solution:
    def isHappy(self, n: int) -> bool:
        original = n 
   

        seen = []
        def process(num) : 
            new_num = 0 
            while num > 0 : 
                new_num += (num % 10)**2
                num = num//10
            # print(new_num)
            # print(seen)

            if new_num == 1 : 
                return True
            if new_num in seen : 
                return False 
            
            seen.append(new_num)
            return process(new_num)
        

            
        return process(n)