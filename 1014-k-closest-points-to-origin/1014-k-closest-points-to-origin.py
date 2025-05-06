class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqrt_list = [(i[0]**2 + i[1]**2) for i in points]
        table = {}

        for i in range(len(sqrt_list)):
            if sqrt_list[i] in table:
                table[sqrt_list[i]].append(i)
            else:
                table[sqrt_list[i]] = [i]
         
        finalists = sorted(table.keys())[:k]
       
        result = []
        last_key = -1
        temp = []
        for i in range(k): 
            if len(temp) >= k : break;
            if finalists[i] in table.keys():
                temp.extend(table[finalists[i]])
                
        result.extend([points[temp[i]] for i in range(len(temp))])
                                    
        return result

        
        
       
        