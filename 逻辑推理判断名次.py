import random

declares = [
    {2:'D', 3:'B'},
    {2:'C', 4:'E'},
    {1:'E', 5:'A'},
    {3:'C', 4:'A'},
    {2:'B', 5:'D'}
]
ls = ['A','B','C','D','E']
found = False
while True:
    random.shuffle(ls)
    pass_count = 0
    for declare in declares:
        truth = 0
        for key in declare:
            if ls[key-1] == declare[key]:
                truth += 1
        if truth != 1:
            break
        else:
            pass_count += 1
    if pass_count == len(declares):
        print(ls)
        break
