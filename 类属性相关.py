class A:
    para = 0
    def __init__(self):
        A.para += 1
        self.para += 1

class B(A):
    pass

if __name__ == "__main__":
    a = A()
    b1 = B()
    b2 = B()
    b3 = B()

    print(a.para)
    print(b3.para)
    print(A.para)
    print(B.para)
