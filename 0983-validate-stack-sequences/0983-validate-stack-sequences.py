class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        for p in pushed : 
            stack.append(p)
            while stack and popped and stack[-1] == popped[0] : 
                stack.pop()
                popped.pop(0)
        return stack == popped == []