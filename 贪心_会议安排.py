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
            timePoint = program.end
    return ret

if __name__ == "__main__":
    p = []
    p.append(Program(6, 12))
    p.append(Program(7, 8))
    p.append(Program(8, 9))
    p.sort()
    print(bestArrange(p,0))