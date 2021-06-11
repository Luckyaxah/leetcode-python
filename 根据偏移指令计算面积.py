import sys
if __name__ == "__main__":
    # 读取第一行的n
    
    firstline = sys.stdin.readline().strip().split(' ')
    N, E = int(firstline[0]), int(firstline[1])

    # ##
    # N = 4
    # E = 10
    # data = [
    #     '1 1',
    #     '2 1',
    #     '3 1',
    #     '4 -2'
    # ]
    # ##
    ops = []
    for i in range(N):
        # line =  data[i]
        line = sys.stdin.readline()

        ops.append(list(map(int, line.strip().split(' '))))
    area = 0
    x = 0
    y = 0

    for op in ops:
        if y == 0:
            x = op[0]
            y = op[1]
        elif y > 0:
            area += (op[0]-x)*y
            x = op[0]
            y += op[1]
        else:
            area += (op[0]-x)*(-y)
            x = op[0]
            y += op[1]
    area += (E-x) * (y if y>0 else -y)
    print(area)