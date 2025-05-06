def merge(arr_one, arr_two):
    temp = [0] * (len(arr_one) + len(arr_two))
    temp_ptr = 0
    L = 0
    R = 0

    while L < len(arr_one) and R < len(arr_two) : 
        if arr_one[L] > arr_two[R]:
            temp[temp_ptr] = arr_two[R]
            R += 1
        else : 
            temp[temp_ptr] = arr_one[L]
            L += 1
        temp_ptr += 1

    while L < len(arr_one):
        temp[temp_ptr] = arr_one[L]
        L += 1
        temp_ptr += 1
    
    while R < len(arr_two): 
        temp[temp_ptr] = arr_two[R]
        R += 1
        temp_ptr += 1 
    
    return temp

def merge_sort(arr):
    arr = list(arr)
    if len(arr) <= 1 : 
        return arr
    mid = len(arr)//2

    arr_one = merge_sort(arr[: mid])
    arr_two = merge_sort(arr[mid:])

    return merge(arr_one, arr_two)
    

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqrt_list = [(i[0]**2 + i[1]**2) for i in points]
        table = {}

        for i in range(len(sqrt_list)):
            if sqrt_list[i] in table:
                table[sqrt_list[i]].append(i)
            else:
                table[sqrt_list[i]] = [i]


        finalists = merge_sort(table.keys())[:k]
        
        temp = []
        for i in range(k): 
            if not len(temp) >= k:
                temp.extend(table[finalists[i]])
                          
        return [points[temp[i]] for i in range(len(temp))][:k]

        
        
       
        