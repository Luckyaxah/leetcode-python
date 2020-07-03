class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        dist = 0
        while z:
            z = z & z-1
            dist += 1
        return dist

if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hammingDistance(x,y))