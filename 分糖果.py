class Solution:
    def distributeCandies(self, candies) -> int:
        s = set(candies)
        p = len(s)
        t = len(candies)//2
        if p > t:
            return t
        else:
            return p
        

if __name__ == "__main__":
    candies = [1,1,2,3]
    print(Solution().distributeCandies(candies))