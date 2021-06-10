class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(image, x, y, color, newColor):

            rows = len(image)
            cols = len(image[0])
            if x<0 or x>=rows:
                return
            if y<0 or y>=cols:
                return
            if image[x][y] != color:
                return
            image[x][y] = newColor
            dfs(image, x-1, y, color, newColor)
            dfs(image, x+1, y, color, newColor)
            dfs(image, x, y-1, color, newColor)
            dfs(image, x, y+1, color, newColor)
        dfs(image, sr, sc, color, newColor)
        return image

Solution().floodFill([[0,0,0],[0,1,0]],1,1,1)