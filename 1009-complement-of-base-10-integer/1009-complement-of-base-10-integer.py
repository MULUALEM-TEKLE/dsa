class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary_string = bin(n)[2:]
        mask = int('1'*len(binary_string) , 2)
        return n ^ mask