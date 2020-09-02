from collections import defaultdict
from typing import List

'''
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''

class Solution:
    # 这样操作是为了数值稳定，当分母大于分子时，对于较小的数，精度容易丢失
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:return len(points)
        slope = defaultdict(lambda :defaultdict(list))
        for i in range(1,len(points)):
            for j in range(i):
                if points[i][0] == points[j][0] :
                    k = '00'
                elif points[i][1] == points[j][1]:
                    k = '01'
                elif abs(points[i][1] - points[j][1]) > abs(points[i][0] - points[j][0]):
                    k = str((points[i][1] - points[j][1]) / (points[i][0] - points[j][0]))+'0'
                else:
                    k = str((points[i][0] - points[j][0]) / (points[i][1] - points[j][1]))+'1'
                slope[k][i].append(j)
                slope[k][j].append(i)
        # print(slope)
        maxP = 2
        def dfs(graph,visited,node):
            if not visited[node]:
                res = 1
                visited[node] = True
                for i in graph[node]:
                    res += dfs(graph,visited,i)
                return res
            return 0


        for k, graph in slope.items():
            visited = {k:False for k in graph.keys()}
            if len(visited) < maxP:
                continue
            for node in graph.keys():
                maxP = max(maxP, dfs(graph,visited,node))
        return maxP

    def maxPoints1(self, points: List[List[int]]) -> int:
        def max_points_on_a_line_containing_point_i(i):
            # init lines passing through point i
            lines, horisontal_lines = {}, 1
            # One starts with just one point on a line : point i.
            count = 1
            # There is no duplicates of a point i so far.
            duplicates = 0
            # Compute lines passing through point i (fixed)
            # and point j (interation).
            # Update in a loop the number of points on a line
            # and the number of duplicates of point i.
            for j in range(i + 1, n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                # add a duplicate point
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue
                # add a horisontal line : y = const
                elif y1 == y2:
                    slope = float('inf')
                # add a line : x = slope * y + c
                # only slope is needed for a hash-map
                # since we always start from the same point
                else:
                    slope = (x1 - x2) / (y1 - y2)
                lines[slope] = lines.get(slope, 1) + 1
                count = max(lines[slope], count)
            print(lines)

            return count + duplicates
        n = len(points)
        if n < 3:
            return n

        max_count = 1
        # Compute in a loop a max number of points
        # on a line containing point i.
        for i in range(n - 1):
            max_count = max(max_points_on_a_line_containing_point_i(i), max_count)
        return max_count

points = [[0,0],[1,1],[0,0]]
print(Solution().maxPoints1(points))
print(Solution().maxPoints(points))
