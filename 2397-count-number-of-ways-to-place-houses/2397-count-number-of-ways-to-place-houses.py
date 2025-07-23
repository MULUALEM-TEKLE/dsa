class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def place(i) : 
            if i == 0 : return 1 
            if i == 1 : return 2

            return (place(i-1) + place(i-2)) 
        
        return (place(n) * place(n) ) % ((10**9)+7)  