from 并查集 import UnionFindSet

# class Position:
#     def __init__(self, r, c):
#         self.row = r
#         self.col = c

def countIslans(l:list):
    positionList = []
    # Map = {}
    for row in range(len(l)):
        for col in range(len(l[0])):
            if l[row][col] == 1:
                position = (row, col)
                positionList.append(position)
    unionSet = UnionFindSet(positionList)
    for row in range(len(l)):
        for col in range(len(l[0])):
            if l[row][col] == 1:
                position = (row, col)
                # 只对上和左合并
                if row-1>=0 and l[row-1][col] ==1:
                    up = (row-1, col)
                    unionSet.union(position, up)
                # if row+1 < len(l) and l[row+1][col] == 1:
                #     down = (row+1, col)
                #     unionSet.union(position, down)
                if col-1>=0 and l[row][col-1] ==1:
                    left = (row, col-1)
                    unionSet.union(position, left)
                # if col+1 < len(l) and l[row][col+1] == 1:
                #     right = (row, col+1)
                #     unionSet.union(position, right)
    return unionSet.getSizeNum()

if __name__ == "__main__":
    m = [
        [0,0,1,0,1,0],
        [1,1,1,0,1,0],
        [1,0,0,1,0,0],
        [0,0,0,0,0,0],
    ]
    print(countIslans(m))
