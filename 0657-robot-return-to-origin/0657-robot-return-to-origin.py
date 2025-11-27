class Solution:
    def judgeCircle(self, moves: str) -> bool:
        table = Counter(moves)

        return table["U"] == table["D"] and table["L"] == table["R"]