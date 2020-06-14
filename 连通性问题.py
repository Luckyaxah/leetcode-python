# n = int(input())

# array = list()
# for r in range(n):
#     a=[int(c) for c in input().split()]
#     array.append(a)

n = 5
# array =[
#     [0,0,0,0,0],
#     [0,1,0,1,0],
#     [1,1,0,1,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0]
# ]
array =[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
]

def isInSameRange(ps1,ps2):
    for p1 in ps1:
        for p2 in ps2:
            if abs(p1[0]-p2[0])<=1 and abs(p1[1]-p2[1])<=1:
                return True
    return False

points = list()
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            points.append([(i,j)])

i = 0
while i < len(points):
    j = i+1
    while j<len(points):
        if isInSameRange(points[i],points[j]):
            points[i]=points[i]+points[j]
            points.pop(j)
            j = i+1
        else:
            j += 1
    i += 1

print(points)
print(len(points))
