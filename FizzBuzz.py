class Solution:
    def fizzBuzz(self, n: int):
        ret = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1)%5 == 0:
                item = 'FizzBuzz'
            elif (i+1)%3 ==0:
                item = 'Fizz'
            elif (i+1)%5 == 0:
                item = 'Buzz'
            else:
                item = '%d' % (i+1)
            ret.append(item)
        return ret

if __name__ == "__main__":
    a = Solution()
    print(a.fizzBuzz(15))