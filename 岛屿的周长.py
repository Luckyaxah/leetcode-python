class Solution:
    def islandPerimeter(self, grid) -> int:
        if not grid:
            return 0
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    edge = 4
                    if i > 0 and grid[i-1][j] == 1:
                        edge -= 1
                    if i < len(grid) -1 and grid[i+1][j] == 1:
                        edge -= 1
                    if j > 0 and grid[i][j-1] == 1:
                        edge -= 1
                    if j < len(grid[0]) -1 and grid[i][j+1] == 1:
                        edge -= 1
                    ret += edge
        return ret
                

if __name__ == "__main__":
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    print(Solution().islandPerimeter(grid))