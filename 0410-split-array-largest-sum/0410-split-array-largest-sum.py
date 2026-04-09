class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low , high = max(nums) , sum(nums)

        if len(nums) == k : return max(nums)
        if k == 1 : return sum(nums)
        ans = 0

        while low <= high : 
            mid = (low+high)//2

            k_ = 1
            acc = 0 
            min_acc = float('-inf')
            split = []
            sub = []
            # print(mid)
            for num in nums : 
                
                if acc + num >= mid : 
                    k_ += 1 
                    acc = 0 
                    split.append(sub)
                    sub = []
                    # continue
                sub.append(num)
                acc += num 
                min_acc = max(min_acc , acc)

            split.append(sub)
            sub = []
            
            print(split)
            # split = []
            
            if k_ <= k : 
                ans = min_acc
                high = mid -1 
           
            else : 
                low = mid + 1 
        
        return ans