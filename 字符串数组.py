def fun(string, strings):
    for item in strings:
        matchedCount = 0
        for char in string:
            if char == item[matchedCount]:
                matchedCount += 1
            else:
                matchedCount = 0
            if matchedCount == len(item):
                return True
    return False

if __name__ == '__main__':
    print(fun('xsdfc',['abx','sdf','edf']))
    print(fun('edxf',['abx','sdf','edf']))

