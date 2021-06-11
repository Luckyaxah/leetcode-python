class Solution:
    def rotatedDigits(self, n: int) -> int:
        d = {
            '0':'0',
            '1':'1',
            '8':'8',
            '2':'5',
            '5':'2',
            '6':'9',
            '9':'6'
        }
        count = 0
        for i in range(1, n+1):
            s = ''
            t = str(i)
            for c in t:
                if c not in d:
                    s =''
                    break
                s += d[c]
            if s and s.isnumeric() and s!= t:
                # print(s)
                count += 1
        return count

print(Solution().rotatedDigits(10))