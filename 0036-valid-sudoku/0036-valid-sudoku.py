class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = cols = 9 
        box_starts = [
            [0 , 0] , [0 , 3] , [0 , 6] , 
            [3 , 0] , [3 , 3] , [3 , 6] , 
            [6 , 0] , [6 , 3] , [6 , 6] , 
        ]

        def check_and_add(value , seen_set) : 
            if value == '.' : 
                    return True
            else : 
                if value in seen : return False
                seen.add(value)
                return True

        for r in range(rows) : 
            seen = set()
            for c in range(cols) : 
                value = board[r][c]
                # if value == '.' : 
                #     continue
                # else : 
                #     if value in seen : return False
                #     seen.add(value)
                if not check_and_add(value , seen) : return False 
        
        for c in range(cols) : 
            seen = set()
            for r in range(rows) : 
                value = board[r][c]
                if value == '.' : 
                    continue
                else : 
                    if value in seen : return False
                    seen.add(value)
        
        for i , j in box_starts : 
            seen = set()
            for r in range(i , i+3) : 
                for c in range(j , j+3) : 
                    value = board[r][c] 
                    if value == "." : 
                        continue 
                    else : 
                        if value in seen : return False
                        seen.add(value)
        return True 