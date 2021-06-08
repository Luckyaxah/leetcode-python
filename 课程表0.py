# 每门课都只有一个先导课程
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        flags = [True for i in range(numCourses)]
        for pair in prerequisites:
            flags[pair[0]] = False
        for i in flags:
            if i == True:
                numCourses -= 1
        count = numCourses
        while count!= 0 and count == numCourses:
            for pair in prerequisites:
                if flags[pair[0]] == False and flags[pair[1]] == True :
                    flags[pair[0]] = True
                    numCourses -= 1
                    break
            count -= 1
            
        if numCourses == 0:
            return True
        return False


# numCourses = 2
# prerequisites = [[1,0],[0,1]]
numCourses = 2
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses, prerequisites))



