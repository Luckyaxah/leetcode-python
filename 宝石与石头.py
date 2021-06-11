class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l = list(jewels)
        ret = 0
        for stone in stones:
            if stone in l:
                ret += 1
        return ret

print(Solution().numJewelsInStones("aA","aAAbbbb"))