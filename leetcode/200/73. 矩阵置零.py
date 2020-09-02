from typing import List

'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
'''
class Solution:
    # 还可以使用矩阵中不存在的一个数字作为标记
    # 使用二进制数作为标记
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=col=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row|=(1<<i)
                    col|=(1<<j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row&(1<<i) or col&(1<<j):
                    matrix[i][j]=0


    # 使用第一行来作为标记，然后为第一行是否为0做一个标记
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=0 in matrix[0]
        col=False
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if matrix[0][0]==0:
            for i in range(1,len(matrix)): matrix[i][0] = 0
        if row:
            for i in range(len(matrix[0])):matrix[0][i]=0


matrix=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Solution().setZeroes(matrix)
for i in matrix:
    print(i)