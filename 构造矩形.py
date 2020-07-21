class Solution:
    def constructRectangle(self, area: int):
        n = int(area ** 0.5) + 1
        min_ = area
        for i in range(1, n):
            if area % i == 0:
                j = area // i
                if j - i < min_:
                    min_ = j-i
                    ret = (j, i)
        return ret

if __name__ == "__main__":
    print(Solution().constructRectangle(4))
    print(Solution().constructRectangle(15))