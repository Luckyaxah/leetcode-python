class Solution:
    def numberOfBoomerangs1(self, points) -> int:
        def dist(x,y):
            sum = 0
            for i,j in zip(x,y):
                sum+=(i-j)**2
            return sum ** 0.5
        l = len(points)
        count = 0
        for i in range(l):
            for j in range(l):
                for k in range(j+1,l):
                    if dist(points[i],points[j]) == dist(points[i],points[k]):
                        print(points[i],points[j],points[k])
                        count += 1
        return count * 2

    def numberOfBoomerangs2(self, points) -> int:
        def dist(x,y):
            sum = 0
            for i,j in zip(x,y):
                sum+=(i-j)**2
            return sum ** 0.5
        l = len(points)
        count = 0
        for i in range(l):
            for j in range(l):
                d_ij= dist(points[i],points[j])
                for k in range(j+1,l):
                    if dist(points[i],points[k]) == d_ij:
                        print(points[i],points[j],points[k])
                        count += 1
        return count * 2

    def numberOfBoomerangs3(self, points) -> int:
        def dist(x,y):
            sum = 0
            for i,j in zip(x,y):
                sum+=(i-j)**2
            return sum ** 0.5
        l = len(points)
        count = 0
        d = {}
        for i in range(l):
            for j in range(l):
                if (i,j) in d:
                    d_ij = d[(i,j)]
                elif (j,i) in d:
                    d_ij = d[(j,i)]
                else:
                    d[(i,j)] = dist(points[i],points[j])
                    d_ij =  d[(i,j)]
                # d_ij= dist(points[i],points[j])
                for k in range(j+1,l):
                    if (i,k) in d:
                        d_ik = d[(i,k)]
                    elif (k,i) in d:
                        d_ik = d[(k,i)]
                    else:
                        d[(i,k)] = dist(points[i],points[k])
                        d_ik =  d[(i,k)]
                    if d_ik == d_ij:
                        print(points[i],points[j],points[k])
                        count += 1
        return count * 2

    def numberOfBoomerangs4(self, points) -> int:
        def dist(x,y):
            return (x[0]-y[0])**2 +(x[1]-y[1])**2
        l = len(points)
        count = 0
        d = {}
        for i in range(l):
            for j in range(l):
                if (i,j) in d:
                    d_ij = d[(i,j)]
                elif (j,i) in d:
                    d_ij = d[(j,i)]
                else:
                    d[(i,j)] = dist(points[i],points[j])
                    d_ij =  d[(i,j)]
                for k in range(j+1,l):
                    if (i,k) in d:
                        d_ik = d[(i,k)]
                    elif (k,i) in d:
                        d_ik = d[(k,i)]
                    else:
                        d[(i,k)] = dist(points[i],points[k])
                        d_ik =  d[(i,k)]
                    if d_ik == d_ij:
                        print(points[i],points[j],points[k])
                        count += 1
        return count * 2

    def numberOfBoomerangs5(self, points) -> int:
        def dist(x,y):
            return (x[0]-y[0])**2 +(x[1]-y[1])**2
        l = len(points)
        count = 0
        d = {}
        for i in range(l):
            for j in range(i+1,l):
                d[(i,j)] = dist(points[i],points[j])
        for i,j in d:
            temp = 0
            for k in range(j+1,l):
                if d[(i,j)] == d[(i,k)]:
                    temp += 1
                if d[(i,j)] == d[(j,k)] :
                    temp += 1
            for k in range(i+1,j):
                if d[(i,j)] == d[(k,j)] :
                    temp += 1
            count += temp
        return count*2

    def numberOfBoomerangs(self, points) -> int:
        def dist(x,y):
            return (x[0]-y[0])**2 +(x[1]-y[1])**2
        l = len(points)
        count = 0
        d = {}
        d1 = {}
        for i in range(l):
            d1[i] ={}
        
        for i in range(l):
            for j in range(i+1,l):
                d[(i,j)] = dist(points[i],points[j])
                if d[(i,j)] in d1[i]:
                    d1[i][d[(i,j)]] += 1
                else:
                    d1[i][d[(i,j)]] = 1
                
                d[(j,i)] = d[(i,j)]
                if d[(i,j)] in d1[j]:
                    d1[j][d[(i,j)]] += 1
                else:
                    d1[j][d[(i,j)]] = 1
            for k in d1[i]:
                if d1[i][k] > 1:
                    count += d1[i][k]*(d1[i][k]-1)
            del d1[i]
        # print(d1)
        return count


if __name__ == "__main__":
    a = Solution()
    print(a.numberOfBoomerangs([[1,0],[0,0],[2,0],[1,1],[-1,0]]))