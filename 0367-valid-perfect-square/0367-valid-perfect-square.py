class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 : return True 
        test = num // 2
        while True: 
            print(test)
            if test * test > num : 
                test = test//2
                continue
            elif test * test == num : 
                return True
            else : 
                break
        
        for i in range(test, num) : 
            if i * i > num : 
                return False
            if i * i == num : 
                return True

        