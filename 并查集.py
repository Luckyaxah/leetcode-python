class UnionFindSet:
    def __init__(self, value_list):
        self.elementMap = {} # 点和节点的对应关系，相当于一个注册表
        self.fatherMap = {} # 父节点对映关系
        self.sizeMap = {} # sizeMap中每一个key都是集合的头节点，也叫做代表节点
        for v in value_list:
            element = Element(v)
            self.elementMap[v] = element
            self.fatherMap[element] = element
            self.sizeMap[element] = 1

    def findHead(self, element):
        # 从element出发，找到不能再网上的头节点
        # 把网上找沿途的路径全都记录下来
        path = []
        while element != self.fatherMap[element]:
            path.append(element)
            element = self.fatherMap[element]
        while path:
            self.fatherMap[path.pop()] = element
        return element

    def isSameSet(self, a, b):
        if a in self.elementMap and b in self.elementMap:
            return self.findHead(self.elementMap.get(a)) == self.findHead(self.elementMap.get(b))

    def union(self, a, b):
        if a in self.elementMap and b in self.elementMap:
            aF = self.findHead(self.elementMap.get(a))
            bF = self.findHead(self.elementMap.get(b))
            if aF != bF:
                big = aF if self.sizeMap.get(aF) >= self.sizeMap.get(bF) else bF
                small = bF if big == aF else aF
                self.fatherMap[small] = big
                self.sizeMap[big] = self.sizeMap[aF] = self.sizeMap[bF]
                del self.sizeMap[small]

class Element:
    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    a = UnionFindSet([1,2,4,5,3])
    