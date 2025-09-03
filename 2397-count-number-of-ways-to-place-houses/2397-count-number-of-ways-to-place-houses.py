class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        cache = {0 : 1 , 1 : 2}
        def place(n) : 
            if n in cache : return cache[n]

            cache[n] = place(n-1) + place(n-2)

            return cache[n]
        
        return (place(n) * place(n)) % MOD