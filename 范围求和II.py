class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        """
        在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
        """
        min_x = m
        min_y = n
        for op in ops:
            min_x = min(min_x, op[0])
            min_y = min(min_y, op[1])
        return min_x * min_y

if __name__ == "__main__":
    m = 3
    n = 3
    operations = [
        [2,2],
        [3,3]
    ]
    print(Solution().maxCount(m,n, operations))