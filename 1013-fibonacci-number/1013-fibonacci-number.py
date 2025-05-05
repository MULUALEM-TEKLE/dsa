class Solution:
    def fib(self, n: int) -> int:
        # if n <= 1 :
        #     return n 

        # return self.fib(n-1) + self.fib(n-2)
        if n <= 0 : 
            return 0
        if n == 1 : 
            return 1
        else :
            a, b = 0, 1
            for i in range(2, n + 1):
                next_fib = a + b
                a, b = b, next_fib

            return b





        