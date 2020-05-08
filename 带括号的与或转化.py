def trans(string):
    symbolList = []
    postFixExpression = []
    for char in string:
        if char >= 'A' and char <= 'Z':
            postFixExpression.append(char)
        elif char == ')':
            symbol = symbolList.pop()
            while symbol != '(':
                postFixExpression.append(symbol)
                symbol = symbolList.pop()
        else:
            if  symbolList and char != '(' and symbolList[-1]!= '(':
                while True:
                    if (not symbolList) or symbolList[-1] == '(':
                        break
                    postFixExpression.append(symbolList.pop())
            symbolList.append(char)
    while(symbolList):
        symbol = symbolList.pop()
        postFixExpression.append(symbol)
    print(postFixExpression)

    result=[]
    for char in postFixExpression:
        print(result)
        if char >= 'A' and char <= 'Z':
            result.append(char)
        else:
            a = result.pop()
            b = result.pop()
        if char == '&':
            result.append( {'must': ['{%s}'%b,'{%s}'%a]} )
        elif char == '|':
            result.append( {'should': ['{%s}'%b,'{%s}'%a]} )
    return result[0]
# def trans(string):
#     charList= []
#     symbolList = []
#     for char in string:
#         if char >= 'A' and char <= 'Z':
#             charList.append(char)
#         else:
#             symbolList.append(char)
#     for char in symbolList:
#         a = charList.pop(0)
#         b =charList.pop(0)
#         if char == '&':
#             charList.insert(0, {'must': ['{%s}'%a,'{%s}'%b]} )
#         elif char == '|':
#             charList.insert(0, {'should': ['{%s}'%a,'{%s}'%b]} )
        
#     return charList[0]

if __name__ == '__main__':
    # print(trans('A&C|D'))
    print(trans('(A&B)&(C|D)'))