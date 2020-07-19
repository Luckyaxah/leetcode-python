import bisect
class Solution:
    def findRadius1(self, houses, heaters) -> int:
        # O(N*M*N*M)
        rads = []
        for house in houses:
            for heater in heaters:
                dist = abs(house-heater)
                if dist not in rads:
                    rads.append(dist)
        rads.sort()
        for rad in rads:
            rad_flag = True
            for house in houses:
                flag = False
                for heater in heaters:
                    lb = heater-rad
                    rb = heater+rad
                    # print(rad, heater, lb,rb, house)
                    if house >= lb and house <= rb:
                        flag = True
                        break
                if flag == False:
                    # 说明当前rad不可用
                    rad_flag = False
                    break
            if rad_flag == True:
                return rad

    def findRadius2(self, houses, heaters) -> int:
        # O(N*M)
        rads = [[None for j in range(len(heaters))] for i in range(len(houses))]
        for i in range(len(houses)):
            for j in range(len(heaters)):
                rads[i][j] = abs(houses[i]-heaters[j])
        mins = [min(rads[i]) for i in range(len(houses)) ]
        print(rads)
        return max(mins)

    def findRadius(self, houses, heaters) -> int:
        houses.sort(); heaters.sort()
        ans = 0
        for house in houses:
            j = bisect.bisect(heaters, house)
            r = float('inf')
            if house >= heaters[0]:
                r = min(r, house - heaters[j - 1])
            if house < heaters[-1]:
                r = min(r, heaters[j] - house)
            ans = max(ans, r)
        return ans

                



if __name__ == "__main__":
    houses = [1,2,3,4,5]
    heaters = [1,4.5]
    print(Solution().findRadius1(houses, heaters))
    print(Solution().findRadius2(houses, heaters))
    print(Solution().findRadius(houses, heaters))
