class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        ds = {}
        dg = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            if not secret[i] in ds:
                ds[secret[i]] = 1
            else:
                ds[secret[i]] += 1

            if not guess[i] in dg:
                dg[guess[i]] = 1
            else:
                dg[guess[i]] += 1
        for key in ds:
            b += min(ds[key],dg.get(key,0))
        b -= a
        
        return "%dA%dB" % (a,b)

if __name__ == "__main__":
    a = Solution()
    print(a.getHint('1807','7810'))
    print(a.getHint('1123','0111'))
    print(a.getHint('1122','2211'))
    print(a.getHint('11','10'))

