class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqrt_list = [(i[0]**2 + i[1]**2) for i in points]
        table = {}

        # for i in range(len(sqrt_list)) : 
        #     if sqrt_list[i] in table.keys() : 
        #         if table[sqrt_list[i]] != i: 
        #             table[sqrt_list[i]] = i
        #             continue
        #     # if sqrt_list[i] not in table.keys():
        #     table[sqrt_list[i]] = i

        for i in range(len(sqrt_list)):
            if sqrt_list[i] in table:
                table[sqrt_list[i]].append(i)
            else:
                table[sqrt_list[i]] = [i]
         

        
        finalists = sorted(table.keys())
        finalists = finalists[:k]

        print(table)


        result = []
        last_key = -1
        temp = []
        for i in range(len(finalists)): 
            if finalists[i] in table.keys():
                if finalists[i] == last_key : 
                    continue
                temp.extend(table[finalists[i]])
                last_key = finalists[i]

        result.extend([points[temp[i]] for i in range(len(temp))])
        print(temp)
                            
        return result[:k]

        
        
       
        