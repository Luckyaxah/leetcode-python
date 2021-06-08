d = {
    '1':[],
    '2':[],
    '3':['1','2'],
    '4':['1'],
    '5':['1','3','4'],
    '6':['5']
}

arr0 = list(d.keys())
arr = []
while arr0:
    for ind, i in enumerate(arr0):
        flag = True
        for j in d[i]:
            if j not in arr:
                flag = False
                break
        if flag == True:
            arr.append(i)
            arr0.pop(ind)
            break
print(arr)

