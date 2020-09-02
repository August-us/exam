# -*- coding:utf-8 -*-
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        for o in range((min(m,n)+1)>>1):
            res.extend([matrix[o][i] for i in range(o,m-o)])
            res.extend([matrix[j][m-1-o] for j in range(o+1,n-o-1)])
            if n-1-o>o:
                res.extend([matrix[n-1-o][m-i-1] for i in range(o,m-o)])
            if m - 1 - o > o:
                res.extend([matrix[n-j-1][o] for j in range(o+1,n-o-1)])
        return res

class Solution1:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        matrix=matrix.copy()  # 拷贝一份，防止修改改变原来的数据
        result = []
        while(matrix):
            result+=matrix.pop(0)
            matrix =list(map(list,zip(*matrix)))[::-1]

        return result



class Solution2:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        n = len(matrix)
        m = len(matrix[0])
        if n == 1 and m == 1:
            res = [matrix[0][0]]
            return res
        for o in range((min(m, n) + 1) // 2):
            [res.append(matrix[o][i]) for i in range(o, m - o)]
            [res.append(matrix[j][m - 1 - o]) for j in range(o, n - o) if matrix[j][m - 1 - o] not in res]
            [res.append(matrix[n - 1 - o][k]) for k in range(m - 1 - o, o - 1, -1) if
             matrix[n - 1 - o][k] not in res]
            [res.append(matrix[l][o]) for l in range(n - 1 - o, o - 1, -1) if matrix[l][o] not in res]
        return res

import numpy as np
from time import time
matrix=np.arange(0,30).reshape(6,-1).tolist()

start=time()
a=(Solution().printMatrix(matrix))
print(time()-start)
print(len(a),a)

# start=time()
# a=(Solution2().printMatrix(matrix))
# print(time()-start)
# print(len(a),a)

start=time()
a=(Solution1().printMatrix(matrix))
print(time()-start)
print(len(a),a)
