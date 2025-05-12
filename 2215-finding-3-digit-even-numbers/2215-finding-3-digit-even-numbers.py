class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # lets create all the possible 3 digit integers from the array
        freq = [0] * 10
        for digit in digits:
            freq[digit] += 1
        result = []

        for i in range(1, 10) : 
            if freq[i] == 0 : continue
            freq[i] -= 1
            for j in range( 10) : 
                if freq[j] == 0 : continue
                freq[j] -= 1 
                for k in range(0, 10 , 2) : 
                    if freq[k] == 0 : continue
                    # freq[k] -= 1 
                    num = (i * 100) + (j * 10) + k
                    result.append(num)
                freq[j] += 1
            freq[i] += 1

        return sorted(result)