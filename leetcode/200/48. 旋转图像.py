from typing import List

'''
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

先转置后翻转
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        for i in range(m):
            for j in range(i,m):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            for j in range(m//2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
        print(matrix)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)

