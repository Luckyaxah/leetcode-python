class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        d = {}
        for pair in prerequisites:
            if pair[0] in d:
                d[pair[0]].append(pair[1])
            else:
                d[pair[0]] = [pair[1]]
        
        flags = [True for i in range(numCourses)]
        for pair in prerequisites:
            flags[pair[0]] = False
        for i in flags:
            if i == True:
                numCourses -= 1

        temp = -1
        while temp != numCourses :
            temp = numCourses
            for key in d.keys():
                if flags[key] == False:
                    ifs = [flags[i] for i in d[key]]
                    if all(ifs):
                        flags[key] = True
                        numCourses -= 1

        if numCourses == 0:
            return True
        if temp == numCourses:
            return False
            
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites) -> bool:
#         d = {}
#         for pair in prerequisites:
#             if pair[0] in d:
#                 d[pair[0]].append(pair[1])
#             else:
#                 d[pair[0]] = [pair[1]]
        
#         flags = [True for i in range(numCourses)]
#         for pair in prerequisites:
#             flags[pair[0]] = False
#         for i in flags:
#             if i == True:
#                 numCourses -= 1

#         count = numCourses
#         while count!= 0 and count == numCourses:
#             for key in d:
#                 ifs = [flags[i] for i in d[key]]
#                 if all(ifs):
#                     flags[key] = True
#                     numCourses -= 1
#                     del d[key]
#                     break
#             count -= 1
            
#         if numCourses == 0:
#             return True
#         return False

# numCourses = 2
# prerequisites = [[1,0],[0,1]]
numCourses = 2
prerequisites = [[1,0]]
# numCourses = 3
# prerequisites = [[1,0],[1,2],[0,1]]
print(Solution().canFinish(numCourses, prerequisites))



