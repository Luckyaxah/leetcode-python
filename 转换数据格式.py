def convert_format(data):
    d = {}
    temp = data
    i = 0
    while temp:
        i = i % len(temp)
        ret = fun(d, temp[i])
        if ret:
            temp.pop(i)
        else:
            i = i+1
    return d


def fun(d, item):
    parent_ind = item.get('parent_ind')
    name = item['name']
    if not parent_ind:
        if not parent_ind in d:
            d[name] = {}
        return True

    for key in d.keys():
        if parent_ind == key:
            d[key][name]={}
            return True
        elif len(d[key].keys() ) != 0:
            ret = fun(d[key], item)
            if ret:
                return True



if __name__ == "__main__":
    industry_list = [
    {
        "parent_ind" : "女装",
        "name" : "连衣裙"
    },
    {
        "name": "女装"
    },
    {
        "parent_ind" : "女装",
        "name" : "半身裙"
    },
    {
        "parent_ind" : "女装",
        "name" : "A字裙"
    },
    {
        "name": "数码"
    },
    {
        "parent_ind" : "数码",
        "name": "电脑配件"
    },
    {
        "parent_ind" : "电脑配件",
        "name": "内存"
    },
    {
        "parent_ind": "内存",
        "name":"1G"
    },
    {
        "parent_ind": "内存",
        "name":"2G"
    },
    {
        "name":"男装"
    }
    ]
    print(convert_format(industry_list))