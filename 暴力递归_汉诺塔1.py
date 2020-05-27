
def LeftToRight(N: int):
    """
    N层汉诺塔从左到右的过程
    """
    if N == 1:
        print("Move 1 From Left to Right.")
        return
    else:
        LeftToMid(N-1)
        print("Move %d from Left to Right." % N)
        MidToRight(N-1)

def LeftToMid(N):
    if N == 1:
        print("Move 1 From Left to Mid")
        return
    else:
        LeftToRight(N-1)
        print("Move %d from Left to Mid" % N)
        RightToMid(N-1)

def MidToRight(N):
    if N == 1:
        print("Move 1 From Mid to Right")
        return
    else:
        MidToLeft(N-1)
        print("Move %d from Mid to Right" % N)
        LeftToRight(N-1)

def RightToMid(N):
    if N == 1:
        print("Move 1 From Right to Mid")
        return
    else:
        RightToLeft(N-1)
        print("Move %d from Right to Mid" % N)
        LeftToMid(N-1)

def MidToLeft(N):
    if N == 1:
        print("Move 1 From Mid to Left")
        return
    else:
        MidToRight(N-1)
        print("Move %d from Mid to Left" % N)
        RightToLeft(N-1)

def RightToLeft(N):
    if N == 1:
        print("Move 1 From Right to Left")
        return
    else:
        RightToMid(N-1)
        print("Move %d from Right to Left" % N)
        MidToLeft(N-1)

if __name__ == "__main__":
    LeftToRight(3)