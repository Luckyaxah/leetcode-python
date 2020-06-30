lst_floor = [1,4,2,5,7,3]
l = []
for i in range(1,len(lst_floor)):
    l.append(lst_floor[i]-lst_floor[i-1])
pl = []
for i in l:
    if i>0:
        pl.extend([chr(8593) for j in range(i)])
    else:
        pl.extend([chr(8595) for j in range(-i)])
print(''.join(pl))