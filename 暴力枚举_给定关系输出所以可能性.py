# 给一长串 input， 每个 input 是两个字符，比如 {A, B} 代表 B 是 A 的 parent 。
# 要求输入所有的字符，每个 child 一定要出现在它的 parent 之后，
# 如果有多种可能性，输出所有组合。

# 举个例子：

# 输入:
# a -> b
# c -> b
# a -> c
# a -> z
# x -> y

# 输出：
# 1）z b c a y x  
# 2）b z c a y x
# 3) y b z c a x 
# 还有其他可能组合，唯一的要求是 child 在 parent 之后
# 注意：

# input 没有环
relations = [
    {'a':'b'},
    {'c':'b'},
    {'a':'c'},
    {'a':'z'},
    {'x':'y'}
]
def fun(relations):
    nodes = list()
    for relation in relations:
        son = list(relation.keys())[0]
        father = list(relation.values())[0]
        if son not in nodes:
            nodes.append(son)
        if father not in nodes:
            nodes.append(father)
    from itertools import permutations
    result = []
    for item in permutations(nodes):
        is_pass = True
        for relation in relations:
            son = list(relation.keys())[0]
            father = list(relation.values())[0]
            if item.index(son) < item.index(father):
                is_pass = False
                # print('bad:',item)
                break
        if is_pass:
            print('good:',item)
            result.append(item)
    return result


print(fun(relations))