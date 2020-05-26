from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        p = []
        for i in events:
            p.append(Program(i[0], i[1]))
        p.sort()
        return bestArrange(p,0)

class Program:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __lt__(self, other):
        return self.end < other.end

def bestArrange(programs, timePoint ):
    programs.sort()

    ret = 0
    for program in programs:
        if timePoint <= program.start:
            ret += 1
            timePoint = program.start+1
    return ret

if __name__ == "__main__":
    pass