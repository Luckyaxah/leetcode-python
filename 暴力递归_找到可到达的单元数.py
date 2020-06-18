def process(arr, i, j, points):
    if not arr or i == -1 or i == len(arr) or j == -1 or j == len(arr[0]):
        return 
    if arr[i][j] != '#':
        return 
    # total += 1
    if (i, j) not in points:
        points.append((i,j))
        process(arr, i, j-1, points)
        process(arr, i-1, j, points)
        process(arr, i+1, j, points)
        process(arr, i, j+1, points)

maps = [
    ['#','*','#','*'],
    ['*','#','#','#'],
    ['#','*','*','#']
]

points = list()
process(maps, 1,3, points)
print(len(points), points)

points = list()
process(maps, 0,0, points)
print(len(points),points)

points = list()
process(maps, 0,1, points)
print(len(points),points)