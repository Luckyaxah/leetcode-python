class RandomPool:
    def __init__(self):
        self.keyIndexMap = {}
        self.indexKeyMap = {}
        self.size = 0
    def insert(self, key):
        if not key in self.keyIndexMap:
            self.keyIndexMap[key] = self.size
            self.indexKeyMap[self.size] = key
            self.size += 1
    def delete(self, key):
        if key in self.keyIndexMap:
            deleteIndex = self.keyIndexMap[key]

            self.size -= 1
            lastIndex = self.size
            lastKey = self.indexKeyMap[lastIndex]

            
            self.keyIndexMap[lastKey] = deleteIndex
            self.indexKeyMap[deleteIndex] = lastKey
            del self.keyIndexMap[key]
            del self.indexKeyMap[lastIndex]

    def getRandom(self):
        import random
        if self.size == 0:
            return None
        randomIndex = int(random.random()*self.size) # 0~size-1
        return self.indexKeyMap[randomIndex]


if __name__ == "__main__":
    d = RandomPool()
    d.insert("123")
    d.insert("345")
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())
    print('='*10)
    d.delete("123")
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())
    print(d.getRandom())