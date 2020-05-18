class Solution:
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row_start = 0
        col_start = 0
        row_end = len(matrix)-1
        col_end = len(matrix[0])-1
        def helper(matrix,row_start,row_end,col_start,col_end):
            # print(row_start,row_end,col_start,col_end)
            while row_start<= row_end and col_start<=col_end:
                row_mid = row_start + ((row_end-row_start)>>1)
                col_mid = col_start + ((col_end-col_start)>>1)
                # print(matrix[row_mid][col_mid],row_mid,col_mid)
                if row_start==row_end and col_start==col_end:
                    return matrix[row_start][col_start] == target
                if matrix[row_mid][col_mid]== target:
                    return True
                elif matrix[row_mid][col_mid] > target:
                    return helper(matrix, row_mid, row_end,col_start, col_mid-1) \
                        or helper(matrix, row_start, row_mid-1,col_start, col_end)
                    # col_end = col_mid
                    # row_end = row_mid
                else:
                    return helper(matrix, row_mid+1, row_end,col_start, col_mid) \
                        or helper(matrix, row_start, row_end,col_mid+1, col_end)
            return False
        return helper(matrix,row_start,row_end,col_start,col_end)

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height-1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        return False


if __name__ == "__main__":
    a = Solution()
    mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print(a.searchMatrix(mat, 5))