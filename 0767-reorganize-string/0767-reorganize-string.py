class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)

        max_heap = [[-count , char] for char , count in cnt.items()]
        heapq.heapify(max_heap)

        if -max_heap[0][0] > (len(s)+1) // 2 : return ""

        res = []

        prev_count , prev_char = 0 , ""

        while max_heap : 
            count , char = heapq.heappop(max_heap)
            res.append(char)

            if prev_count < 0 : 
                heapq.heappush(max_heap , [prev_count , prev_char])
            
            count += 1 
            prev_count , prev_char = count , char 
        
        return "".join(res)