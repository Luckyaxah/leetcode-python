class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []


    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        for k in range(len(self.data)):
            if self.data[k] == key:
                self.data.pop(k)
                break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.data:
            return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)