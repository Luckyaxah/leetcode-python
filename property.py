class A:
    def __init__(self):
        self.a = 1
    def get_a(self):
        return self.a
    aaa = property(fget = get_a)

obj = A()
print(obj.aaa)