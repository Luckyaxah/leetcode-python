import sys 
for line in sys.stdin:
    l = ['a', 'e', 'i', 'o', 'u']
    _max = 0
    count = 0
    for c in line.strip():
        if c in l:
            count += 1
        else:
            _max = max(count, _max)
            count = 0
    print(_max)