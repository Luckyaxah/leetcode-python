# 给定head和所有查询语句
class Query:
    # 一个query类的实例表示一条查询语句，一个Query类型的数组ques
    # 返回Node类型的数组 ans, ans[i]代表ques[i]这条查询的答案
    # 既ques[i].o1和ques[i].o2的最近公共祖先
    # 若二叉树节点数为N，查询语句条数为M，时间复杂度要求达到O(N+M)

    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

def tarJanQuery(head, quries):
    queryMap = {}
    indexMap = {}
    ancestorMap = {}
    sets = UnionFindSet(getAllNodes(head))
    ans = [None for i in range(len(quries))]
    setQueriesAndSetEasyAnswers(quries, ans, queryMap, indexMap)

    setAnswers(head, ans, queryMap, indexMap, ancestorMap, sets)
    return ans

# def setAnswers():
#     if head == None:
#         return
    

 