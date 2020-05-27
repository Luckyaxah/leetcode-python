def hanoi(N):
    if N > 0:
        func(N, '左','右','中')

def func(N, _from , _to, _other):
    if N == 1:
        print("Move 1 from %s to %s" % (_from, _to) )
    else:
        func(N-1, _from, _other, _to)
        print("Move %d from %s to %s" %(N, _from, _to))
        func(N-1, _other, _to, _from)


if __name__ == "__main__":
    hanoi(3)