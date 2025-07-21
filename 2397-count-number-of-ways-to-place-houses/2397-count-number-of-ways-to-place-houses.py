class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def place(n) : 
            if n == 0 : return 1
            if n == 1 : return 2
            return  place(n-2) + place(n-1)
        return (place(n) * place(n)) % ((10**9) + 7)
