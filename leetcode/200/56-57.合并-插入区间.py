from typing import List

'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        if not intervals or not intervals[0]:
            return []
        # 排序之后，如果和前面的有重叠，则合并
        res=[intervals[0]]
        for itv in intervals:
            if res[-1][1]>=itv[0]:
                if res[-1][1]<itv[1]:
                    res[-1][1]=itv[1]
            else:
                res.append(itv)
        return res

    '''
    给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 做了太多条件判断，花费了不少时间
        if not intervals:
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i][1]>= newInterval[0]:
                if intervals[i][0] > newInterval[1]:
                    intervals.insert(i,newInterval)
                    return intervals
                elif intervals[i][1] >= newInterval[1]:
                    intervals[i][0]=min(newInterval[0],intervals[i][0])
                    return intervals
                else:
                    intervals[i][0]=min(intervals[i][0],newInterval[0])
                    intervals[i][1]=newInterval[1]
                    j=i+1
                    while j<len(intervals):
                        if intervals[j][0]>newInterval[1]:
                            return intervals
                        elif intervals[j][1]>newInterval[1]:
                            intervals[i][1]=intervals[j][1]
                            intervals.pop(j)
                        else:
                            intervals.pop(j)
                    else:
                        return intervals
        intervals.append(newInterval)
        return intervals
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 该方法由merge函数直接变换而来，本以为会省时间，但是并没有，因为插入之后最多和前面一个合并，和后面多个合并。
        if not intervals:
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[0]:
                intervals.insert(i,newInterval)
                break
        else:
            if intervals[-1][1]>newInterval[0]:
                intervals[-1][1]=max(intervals[-1][1],newInterval[1])
            return intervals

        res = intervals[:max(i,1)]

        for j in range(i,len(intervals)):
            if res[-1][1] >= intervals[j][0]:
                if res[-1][1] < intervals[j][1]:
                    res[-1][1] = intervals[j][1]
            elif j==i:
                res.append(intervals[j])
            else:
                res+=intervals[j:]
                return res
        return res




a=[[0,5],[9,12]]
print(Solution().insert1(a,[7,16]))