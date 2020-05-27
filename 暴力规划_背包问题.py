def process(w, v, index, alreadyW, bag):
    # w[index]当前货物的重量, v[index]当前货物的价值
    # index 当前来到的货物号
    # alreadyW 目前形成的重量
    # bag 袋子的总重量
    if alreadyW >bag:
        return -1
    
    if index == len(w):
        return 0
    
    p1 = process(w, v, index+1, alreadyW, bag)

    p2next = process(w, v, index+1 , alreadyW+w[index], bag)

    p2 = -1
    if p2next != -1:
        p2 = v[index] + p2next

    return max(p1, p2)


if __name__ == "__main__":
    w = [1,2,3,4]
    v = [5,4,3,2]
    bag = 4
    print(process(w, v, 0, 0, bag))