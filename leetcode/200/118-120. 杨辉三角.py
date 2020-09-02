from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
        # 注意这里的下标是从1开始，和下面的函数不一致

        res = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1,0,-1):
                res[j] += res[j-1]
        return res[:rowIndex+1]

    def generate(self, numRows: int) -> List[List[int]]:
        # 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
        res = [[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j]= res[i-1][j-1] +res[i-1][j]
        return res

    def getRow_(self, rowIndex: int) -> List[int]:
        res = [[1]*(rowIndex+1) for _ in range(2)]
        flag=0
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                res[flag][j] = res[1-flag][j - 1] + res[1-flag][j]
            flag=1-flag
        return res[rowIndex & 1][:rowIndex+1]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
        
        例如，给定三角形：
        
        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
        '''''
        for i in range(1, len(triangle)):
            triangle[i][0] +=triangle[i-1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1:j+1])
            triangle[i][-1] += triangle[i-1][-1]

        return min(triangle[-1])

a=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(Solution().minimumTotal(a))

