class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        for shift in range(-len(matrix)+2,len(matrix[0])-1):
            temp = None
            for i in range(len(matrix)):
                j = i + shift
                if j >= 0 and j < len(matrix[0]):
                    print(i,j,temp, matrix[i][j])
                    if temp == None:
                        temp = matrix[i][j]
                    elif temp != matrix[i][j]:
                        return False
        return True
            
            

# 当且仅当矩阵中每个元素都与其左上角相邻的元素（如果存在）相等时，该矩阵为托普利茨矩阵。因此，我们遍历该矩阵，将每一个元素和它左上角的元素相比对即可。
# class Solution {
# public:
#     bool isToeplitzMatrix(vector<vector<int>>& matrix) {
#         int m = matrix.size(), n = matrix[0].size();
#         for (int i = 1; i < m; i++) {
#             for (int j = 1; j < n; j++) {
#                 if (matrix[i][j] != matrix[i - 1][j - 1]) {
#                     return false;
#                 }
#             }
#         }
#         return true;
#     }
# };


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/toeplitz-matrix/solution/tuo-pu-li-ci-ju-zhen-by-leetcode-solutio-57bb/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。