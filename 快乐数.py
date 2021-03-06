# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

# 如果 n 是快乐数就返回 True ；不是，则返回 False 。

class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(num):
            ret = 0
            while num:
                ret += (num% 10) ** 2
                num =  (num//10) 
            return ret
        while n != 1:
            if n == 4:
                return False
            n = fun(n)
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isHappy(2101))