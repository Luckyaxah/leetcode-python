class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        start = timeSeries[0]
        end = timeSeries[0] + duration
        ret = 0
        for time in timeSeries[1:]:
            if time <= end:
                end = time + duration
            else:
                ret += end - start
                start = time
                end = time + duration
        ret += end - start
        return ret

print(Solution().findPoisonedDuration([1,4], 2))
print(Solution().findPoisonedDuration([1,2], 2))

            
