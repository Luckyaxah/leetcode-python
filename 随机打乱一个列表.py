import random
def shuffle(L):
    random.shuffle(L)


if __name__ == "__main__":
    a = [1,2,3,4]
    shuffle(a)
    print(a)