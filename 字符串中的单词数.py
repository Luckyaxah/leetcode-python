class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        i = 0
        l = len(s)
        flag = 0
        while i< l:
            if s[i]== ' ':
                if flag == 1:
                    count += 1
                    flag = 0
            else:
                if flag == 0:
                    flag = 1
            i += 1
        if flag == 1:
            count += 1
        return count



if __name__ == "__main__":
    a = Solution()
    s = "Hello, my name is John"
    print(a.countSegments(s))