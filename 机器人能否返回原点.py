class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {}
        for move in moves:
            d[move] = d.get(move,0) + 1
        if d.get('L', 0) == d.get('R',0) and \
            d.get('U', 0) == d.get('D',0):
            return True
        return False
