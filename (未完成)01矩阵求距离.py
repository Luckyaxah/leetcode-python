# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
class Solution:
    def updateMatrix(self, matrix):
        pass
    #     def get_dis(mat,i,j):
    #         rows = len(mat)
    #         cols = len(mat[0])
    #         distance = len(mat)
    #         temp = distance
    #         if(mat[i][j]==0):
    #             return 0

    #         d1 = i-1
    #         while d1> -1:
    #             if mat[d1][j] == 0:
    #                 temp = i - d1 
    #                 break
    #             d1 -= 1
    #         if(distance>temp):
    #             distance = temp

    #         d2 = i+1
    #         while d2< rows:
    #             if mat[d2][j] == 0:
    #                 temp = d2-i 
    #                 break
    #             d2 += 1
    #         if(distance>temp):
    #             distance = temp

    #         d3 = j-1
    #         while d3> -1:
    #             if mat[i][d3] == 0:
    #                 temp = j -d3 
    #                 break
    #             d3 -= 1
    #         if(distance>temp):
    #             distance = temp

    #         d4 = j+1
    #         while d4< cols:
    #             if mat[i][d4] == 0:
    #                 temp = d4- j 
    #                 break
    #             d4 += 1
    #         if(distance>temp):
    #             distance = temp

    #         return distance

    #     rows = len(matrix)
    #     if not rows:
    #         return []
    #     cols = len(matrix[0])
    #     ret=[]
    #     for i in range(rows):
    #         ret.append([])
    #         for j in range(cols):
    #             ret[i].append(get_dis(matrix,i,j))
    #     return ret

if __name__ == "__main__":
    a = Solution()
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(a.updateMatrix(mat))