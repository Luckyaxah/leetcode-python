def getRight(num):
    """
    2^4+2=18 -> 10010
    ~18 -> 01101
    ~18+1 -> 01110
    (~18+1) & 18 -> 00010
    """
    return (~num+1) & num

if __name__ == "__main__":
    print(getRight(18))