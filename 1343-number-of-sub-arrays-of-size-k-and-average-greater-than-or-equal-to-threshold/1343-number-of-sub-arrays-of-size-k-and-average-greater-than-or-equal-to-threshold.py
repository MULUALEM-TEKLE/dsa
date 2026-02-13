class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0 
        cur_sum = sum(arr[:k])
        res = 1 if cur_sum/k >= threshold else 0 
        

        for i in range(k , len(arr)) :
            cur_sum += arr[i]
            cur_sum -= arr[left]
            if cur_sum/k >= threshold : 
                # print(f"avg {cur_sum}/{k} >= {threshold}")
                res += 1
            # print(cur_sum)
            left += 1
        return res 