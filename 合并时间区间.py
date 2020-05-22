"""
给定一组不重叠的时间区间，在时间区间中插入一个新的时间区间(如果有重叠的话就合并区间)。
这些时间区间初始是根据它们的开始时间排序的。
示例1:
给定时间区间[1,3]，[6,9]，在这两个时间区间中插入时间区间[2,5]，
并将它与原有的时间区间合并，变成[1,5],[6,9].
示例2：
给定时间区间[1,2],[3,5],[6,7],[8,10],[12,16],在这些时间区间中插入时间区间[4,9]，
并将它与原有的时间区间合并，变成[1,2],[3,10],[12,16].
这是因为时间区间[4,9]覆盖了时间区间[3,5],[6,7],[8,10].
"""

def mergeTimeInterval(intervals, new):
    new_insert = new

        
    l = -1
    r = -1
    for i in range(len(intervals)):
        if intervals[i][0]<new_insert[0]:
            l = i
        if intervals[i][1]<new_insert[1]:
            r = i

    print(l, r)
    if r<l:
        return intervals

    while r>l:
        intervals.pop(r)
        r-=1

    if not intervals:
        intervals.append(new_insert)
        return intervals



    if l+1<len(intervals) and new_insert[1]>=intervals[l+1][0]:
        new_insert = [new_insert[0],intervals.pop(l+1)[1]]
    if l==-1 and r==-1:
        intervals.insert(0, new_insert)
        return intervals 
    if intervals[l][1]<new_insert[0]:
        intervals.insert(l+1, new_insert)
    else:
        new_insert = [intervals[l][0], new_insert[1]]
        intervals.pop(l)
        intervals.insert(l,new_insert)
    return intervals




    

if __name__ == "__main__":
    time_intervals = [[1,5]]
    new_time_interval = [0,3]
    print(time_intervals, new_time_interval)
    mergeTimeInterval(time_intervals, new_time_interval)
    print(time_intervals)

    time_intervals = [[1,5]]
    new_time_interval = [0,0]
    print(time_intervals, new_time_interval)
    mergeTimeInterval(time_intervals, new_time_interval)
    print(time_intervals)

    time_intervals = [[1,5]]
    new_time_interval = [1,3]
    print(time_intervals, new_time_interval)
    mergeTimeInterval(time_intervals, new_time_interval)
    print(time_intervals)