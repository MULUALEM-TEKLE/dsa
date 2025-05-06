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
       

        temp = []
        for i in range(k): 
            if not len(temp) >= k:
                temp.extend(table[finalists[i]])
                          
        return [points[temp[i]] for i in range(len(temp))]

        
        
       
        