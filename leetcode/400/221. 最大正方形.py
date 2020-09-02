from typing import List

'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        r = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = int(matrix[i][j]) * (min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1)
                r = max(r, matrix[i][j])
        return r*r


print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(Solution().maximalSquare([]))

print(Solution().maximalSquare([['1']]))

