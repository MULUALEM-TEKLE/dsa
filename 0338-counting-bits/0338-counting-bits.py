class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        for i in range(1, n+1) : 
            cnt = 0
            while i > 0 : 
                if i & 1 == 1 : 
                    cnt += 1 
                i = i >> 1
            res.append(cnt)
        return res