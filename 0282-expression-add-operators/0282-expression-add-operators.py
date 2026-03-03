class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def explore(index, path , cur_val , prev_val) : 
            if index >= len(num) : 
                if cur_val == target : 
                    res.append(path)
                return
            

            for i in range(index , len(num)) : 
                if i > index and num[index] == '0' : 
                    break
                
                substr = num[index : i+1]
                val = int(substr)

                if index == 0 : 
                    explore(i+1 , substr , val , val)
                else :
                    explore(i+1 , path + '+' + substr , cur_val + val , val)
                    explore(i+1 , path + '-' + substr , cur_val - val , -val)
                    explore(i+1 , path + '*' + substr , (cur_val - prev_val) + (prev_val * val) , prev_val * val)
            
        explore(0 , "" , 0 , 0)

        return res

                
            
