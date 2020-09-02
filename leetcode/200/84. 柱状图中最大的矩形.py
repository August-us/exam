from typing import List

'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

'''
class Solution84:
    def largestRectangleArea_dm(self, heights: List[int],start=0,end=None) -> int:
        # 分治法，而是是多段分治    二段分治则是找到一个最小的，直接在两侧进行分治
        # 复杂度是O(n^2)，可以用线段树优化到O(nlgn)

        if end is None:end=len(heights)
        if start>=end:return 0
        if start==end-1:return heights[start]
        minh=heights[start]
        maxh=heights[start]
        cur=[start]
        for i in range(start+1,end):
            if heights[i]<minh:
                minh=heights[i]
                cur=[i]
            elif heights[i]==minh:
                cur.append(i)
            else:maxh=heights[i]
        res= minh*(end-start)
        start-=1
        for i in cur:
            if (i-start)*maxh<res:
                continue
            res=max(res,self.largestRectangleArea_dm(heights,start+1,i))
            start=i
        res=max(res,self.largestRectangleArea_dm(heights,i+1,end))
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[-1]
        res=0
        for i,num in enumerate(heights):
            while stack[-1]!=-1 and heights[stack[-1]]>=num:
                res=max(res,heights[stack.pop()]*(i-stack[-1]-1))  # 如果当前的高度比之前的小，那么一直往前找，直到找到第一个比它小的高度，这段区间计算面积
            stack.append(i)  # 如果之前的高度比现在的小，那么前面的一定是第一个比当前小的高度
        for i in range(len(stack)-1,0,-1):
            print((len(heights)-stack[i-1]-1)*heights[stack[i]])
            res=max(res,(len(heights)-stack[i-1]-1)*heights[stack[i]])  # 表示从末尾到前面一个的索引，因为前面的索引对应的高度肯定是上一个比它小的
        return res


'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。这道题建立在84的基础上

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6


'''
class Solution85:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        m,n=len(matrix),len(matrix[0])
        width=[[0]*n for i in range(m)]
        for j in range(n): # 求出每一列的元素对应的最大高度
            width[0][j] = int(matrix[0][j] == '1')
            for i in range(1, m):
                width[i][j]= (matrix[i][j] == '1') * (width[i-1][j] + 1)
        res=0
        # for i in width:print(i)
        for i in range(m):
            stack = [-1]
            for j, num in enumerate(width[i]):
                while stack[-1] != -1 and width[i][stack[-1]] >= num:
                    res = max(res,width[i][stack.pop()] * (j - stack[-1] - 1))  # 如果当前的高度比之前的小，那么一直往前找，直到找到第一个比它小的高度，这段区间计算面积
                stack.append(j)  # 如果之前的高度比现在的小，那么前面的一定是第一个比当前小的高度
            for j in range(len(stack) - 1, 0, -1):
                res = max(res, (len(width[i]) - stack[j - 1] - 1) * width[i][stack[j]])  # 表示从末尾到前面一个的索引，因为前面的索引对应的高度肯定是上一个比它小的
        return res

    def maximalRectangle_dp(self, matrix: List[List[str]]) -> int:
        # 方法复杂，详情看leetcode
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n  # 记录左边第一个比当前下标低的下标
        right = [n] * n  # 记录右边边第一个比当前下标低的下标，左右的计算是对称的
        height = [0] * n  # 如果当前的柱子对应的是最大的面积，那么一定可以向两边扩展
        maxarea = 0

        for i in range(m):
            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea


matrix=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(Solution85().maximalRectangle_dp(matrix))


heights=[2,1,5,6,2,3]  # res=10
heights=[1]
heights=[6,7,5,2,4,5,9,3] # res=16
print(Solution84().largestRectangleArea(heights))
