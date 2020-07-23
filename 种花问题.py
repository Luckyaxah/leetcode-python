class Solution:
    def canPlaceFlowers1(self, flowerbed, n: int) -> bool:
        def process(flowerbed):
            if not flowerbed:
                return 0
            if len(flowerbed) == 1:
                if flowerbed[0] == 1:
                    return 0
                else:
                    return 1
            if len(flowerbed) == 2:
                if flowerbed[0]+flowerbed[1]>0:
                    return 0
                else:
                    return 1
            p1 = 0
            if flowerbed[0] == 1:
                p1 = process(flowerbed[2:])
            elif flowerbed[1] == 1:
                p1 = process(flowerbed[3:])
            else:
                p1 = process(flowerbed[2:])+1
                p1 = max(p1, process(flowerbed[1:]))
            return p1
        k = process(flowerbed)
        return k>=n

    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        count = 1
        k = 0
        for i in flowerbed:
            if i == 0:
                count+=1
            else:
                if count > 0:
                    k += (count-1)//2
                count = 0
        if count > 0:
            count += 1
            k += (count-1) //2
        return k>=n


if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    print(Solution().canPlaceFlowers1(flowerbed, n))
    print(Solution().canPlaceFlowers(flowerbed, n))